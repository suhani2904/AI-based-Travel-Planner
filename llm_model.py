from langchain.prompts import PromptTemplate
from typing import List, Dict
from prompts_class import parser_1 , PlacesOutput , parser_2

def extract_places_and_categories_from_llm(llm_output):
    places_list = []
    cat_info: Dict[str, List[str]] = {} 

    for place in llm_output:
        place_name = place.name
        categories = place.category 

        places_list.append(place_name)

        for cat in categories:
            if cat in cat_info:
                cat_info[cat].append(place_name)
            else:
                cat_info[cat] = [place_name]

    return places_list, cat_info

def top_places_from_llm(destination , preferences , llm):
  prompt = PromptTemplate(
    input_variables=["destination", "categories"],
    template=
    """
   You are a travel expert. Your task is to **select the top tourist attractions** in {destination} based on {categories} only, ensuring that only the most popular and highly-rated places are chosen based on google search.
   Give the name and categories of the places and categories must be from {categories} 
  {format_instruction}
    """,
    partial_variables={'format_instruction' : parser_1.get_format_instructions()}
  )
  chain = prompt | llm | parser_1
  return chain.invoke({'destination' : destination ,'categories' : preferences})


def get_llm_places_and_process(destination, preferences, llm):
    llm_output_2 = top_places_from_llm(destination, preferences, llm)
    if isinstance(llm_output_2, PlacesOutput):
        places_objects = llm_output_2.places 
    return extract_places_and_categories_from_llm(places_objects)


def summazies_desc(desc, place , destination , llm):
    template = """
    Write a detailed description of {place} located in {destination} in approximately 300 words.
    
    {desc_clause}

    Ensure the description is engaging, informative, and captures the essence of the place.
    """

    desc_clause = (
        f"Here is the provided description: {desc}\nSummarize it in around 300 words, retaining key details."
        if desc and "Please provide me" not in desc 
        else "No description is available. Provide a brief yet informative overview of this place loacted in {destination}, highlighting its key attractions, history, and significance."
    )

    prompt = template.format(place=place, desc_clause=desc_clause , destination = destination)
    return llm.invoke(prompt)

def ticket_and_rating(places , llm):
    prompt = PromptTemplate(
        input_variables=["places"],
        template="""
        You are an expert travel planner. Your task is to provide ticket prices and ratings of the {places}.
        If ticket price or rating is not available, **estimate based on similar places**.
        {format_instructions}
        """,
        partial_variables={'format_instructions': parser_2.get_format_instructions()} 
    )

    chain = prompt | llm | parser_2  
    
    return chain.invoke({'places' : places}) 


