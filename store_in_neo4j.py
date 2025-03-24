def store_places_in_neo4j(destination, places_info, category , graph):
    for place, info in places_info.items():
        query = f"""
        MERGE (d:Destination {{name: $destination}})
        MERGE (p:Place {{name: $place}})
        MERGE (d)-[:`{category.upper()}`]->(p)
        SET p += $info  
        """
        graph.query(query, params={
            "destination": destination,
            "place": place,
            "info": info,
        })

    return "completed"