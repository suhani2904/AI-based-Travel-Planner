import os
from dotenv import load_dotenv
import concurrent.futures
from langchain_groq import ChatGroq
from neo4j_initializes import Neo4jConnection
from store_in_neo4j import store_places_in_neo4j
from Google_search import get_google_places_and_process
from rag_search_neo4j import search_places_in_neo4j
from Wikipedia.Wikipedia_images import get_wiki_image
from Wikipedia.Wikipedia_content import get_desc_from_wikipedia
from llm_model import get_llm_places_and_process, ticket_and_rating , summazies_desc
from prompts_class import all_places_output

# Load the .env file
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def initializes_llm():
    graph = Neo4jConnection(NEO4J_URI , NEO4J_USERNAME , NEO4J_PASSWORD)
    llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="Gemma2-9b-It")

    return graph, llm


def find_places_stored_in_neo4j(destination, preferences , days ,budget):
    graph, llm = initializes_llm()
    results = []
    for category in preferences:
        query = f"""
        MATCH (d:Destination {{name: $destination}})-[:`{category.upper()}`]->(p:Place)
        RETURN p.name AS place, p.description AS description, p.rating AS rating, p.ticket AS ticket ,p.image AS image
        """
        result = graph.query(query, params={"destination": destination})
        results.extend(result)
    if results == []:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future1 = executor.submit(get_google_places_and_process, destination, preferences, llm)
            future2 = executor.submit(get_llm_places_and_process, destination, preferences, llm)

            # Retrieve results
            google_places_list, cat_info1 = future1.result()
            llm_places_list, cat_info2 = future2.result()

        cat_info = {}
        for key in set(cat_info1) | set(cat_info2):
            cat_info[key] = cat_info1.get(key.strip(), []) + cat_info2.get(key.strip(), [])
        places_list = google_places_list + llm_places_list

        places_info = {}
        for place in places_list:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future3 = executor.submit(get_desc_from_wikipedia ,place )
                future4 = executor.submit(get_wiki_image , place)

                desc = future3.result()
                url = future4.result()

            places_info[place] = {"description" : desc , "image" : url}
        
        for place , info in places_info.items():
            desc = info["description"]
            summary = summazies_desc(desc , place , destination , llm)
            places_info[place]["description"] = summary.content

        places_list = []
        for place , info in places_info.items():
            places_list.append(place)

        rating_and_ticket = ticket_and_rating(places_list , llm)
        if isinstance(rating_and_ticket, all_places_output): 
           places_objects = rating_and_ticket.places

        for place in places_objects:
            place_name = place.name
            t = place.ticket
            r = place.rating
            places_info[place_name]["ticket"] = t
            places_info[place_name]["rating"] = r

        for category, places in cat_info.items():
            for place in places:
                if place in places_list:
                    places_info_1 = {
                        place: {
                            "description": places_info[place]["description"],
                            "rating": places_info[place]["rating"],
                            "ticket": places_info[place]["ticket"],
                            "image": places_info[place]["image"]
                        }
                    }
                store_places_in_neo4j(destination , places_info_1 , category , graph)
        
        result = search_places_in_neo4j(destination , preferences, graph)      
        return result
    else:
        return results

        
    


                
                


        
    
