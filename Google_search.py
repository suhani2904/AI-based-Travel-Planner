import time
import random
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from langchain.prompts import PromptTemplate
from llm_model import extract_places_and_categories_from_llm
from prompts_class import parser_1 , PlacesOutput

def get_google_top_places(city, preferences):

    top_places = []
    headers = {"User-Agent": "Mozilla/5.0"}  

    for preference in preferences:
        query = f"top {preference} places in {city}"

        try:
            search_results = list(search(query, num_results=2))

            for url in search_results:
                try:
                    time.sleep(random.uniform(2, 5))
                    response = requests.get(url, headers=headers)
                    response.raise_for_status()  

                    soup = BeautifulSoup(response.text, "html.parser")
                    headings = [h.get_text().strip() for h in soup.find_all(['h2', 'h3'])]

                    filtered_headings = [
                        h for h in headings if not any(
                            word in h.lower() for word in ["travel", "packages", "hotel", "collection", "ready to plan"]
                        )
                    ]

                    top_places.extend(filtered_headings)

                except Exception as e:
                    print(f"Error processing {url}: {e}")

        except Exception as e:
            print(f"Error performing Google search: {e}")

    return top_places

def llm_search_google_search(destination, all_places  , preferences , llm):
    template  = PromptTemplate( 
    template="""You are a travel expert. Your task is to **select the top tourist attractions** in {destination} from {all_places}, ensuring that only the most popular and highly-rated places are chosen.
    Give the name and categories of the places and categories must be from {categories} 
    {format_instruction}""",
    input_variables=["destination", "all_places", "categories"],
    partial_variables={'format_instruction' : parser_1.get_format_instructions()}
    )

    chain = template | llm | parser_1

    result =  chain.invoke({'destination':destination, 'all_places' :all_places, 'categories' : preferences})
    return result

def get_google_places_and_process(destination, preferences, llm):
    places_by_google_search = get_google_top_places(destination, preferences)
    llm_output_1 = llm_search_google_search(destination, places_by_google_search, preferences, llm)

    if isinstance(llm_output_1, PlacesOutput): 
        places_objects = llm_output_1.places 
    return extract_places_and_categories_from_llm(places_objects)


