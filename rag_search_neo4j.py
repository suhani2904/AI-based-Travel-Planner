def search_places_in_neo4j(destination, preferences , graph):
    results = []
    for category in preferences:
      print(category.upper())
      query = f"""
      MATCH (d:Destination {{name: $destination}})-[:`{category.upper()}`]->(p:Place)
      RETURN p.name AS place, p.description AS description, p.rating AS rating, p.ticket AS ticket , p.image AS image
      """
      result = graph.query(query, params={"destination": destination})
      results.extend(result)

    return results if results else None