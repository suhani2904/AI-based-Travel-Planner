import requests

def get_desc_from_wikipedia(place):
    
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={place}&format=json"
    search_response = requests.get(search_url).json()
    
    if "query" not in search_response or not search_response["query"]["search"]:
        return "No description found."

    # Get the title of the first search result
    best_match_title = search_response["query"]["search"][0]["title"]

    wiki_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exlimit=1&titles={place}&explaintext=1&exsectionformat=plain&exchars={1000}&format=json"
    
    response = requests.get(wiki_url).json()
    
    pages = response.get("query", {}).get("pages", {})
    if not pages:
        return "No description found."
    page = next(iter(pages.values()))
    return page.get("extract", "No description found.")