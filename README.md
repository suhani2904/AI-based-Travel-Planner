#AI-Based Travel Planner 🌍✈️

#Overview
The AI-Based Travel Planner is an intelligent travel assistant that helps users create personalized travel itineraries based on their source, destination, number of days, budget, and preferences. The system integrates LangChain for intelligent query processing, Neo4j for graph-based data storage, and Retrieval-Augmented Generation (RAG) for efficient search. If requested places are not found in Neo4j, the system dynamically fetches LLM-generated insights, Wikipedia descriptions, and images before storing them for future use.

#Features 🚀
✅ User-Centric Itinerary Generation – Users enter their destination, budget, duration, and preferences, and the system generates an optimized itinerary.
✅ AI-Powered Recommendations – The planner suggests historical places, parks, food spots, adventure activities, and more based on user preferences.
✅ RAG-Based Search with Neo4j & LangChain – If places exist in the database, results are fetched quickly; otherwise, new places are retrieved, processed, and stored.
✅ Multi-Source Data Retrieval – The system fetches Wikipedia for descriptions & images, LLM (via LangChain) for structured data, and Google search if needed.
✅ Ticket Price & Rating Estimation – The system intelligently estimates ticket prices and ratings for places.
✅ Interactive Web UI – Built using Flask, HTML, CSS, and JavaScript, with clickable place cards that reveal more details like detail description , rating , ticket price on click.

#Tech Stack 🛠️
🔹 Backend: Flask, Neo4j, Python, LangChain
🔹 Frontend: HTML, CSS, JavaScript
🔹 Database: Neo4j (Graph Database)
🔹 AI & ML: LangChain, Retrieval-Augmented Generation (RAG), LLM (Language Model for text processing), Wikipedia API

#Project Workflow 🛠️
1️⃣ User Input: The user provides a destination, number of days, budget, and preferences.
2️⃣ RAG Search with LangChain & Neo4j: If data exists, fetch and display results instantly.
3️⃣ Data Retrieval: If missing, fetch places via LLM search (LangChain), Wikipedia, and Google search.
4️⃣ Wikipedia API: Extract descriptions and images for the places.
5️⃣ LangChain Processing: Generate ticket prices, ratings, and category-based recommendations.
6️⃣ Store in Neo4j: Save new places for future use.
7️⃣ Display Results: Show the travel itinerary in a structured and visually appealing format.

#Installation & Setup 🛠️
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Travel-Planner.git
cd AI-Travel-Planner
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set Up Environment Variables
Create a .env file and add:
NEO4J_URI=your_neo4j_uri
NEO4J_USERNAME=your_neo4j_username
NEO4J_PASSWORD=your_neo4j_password
GROQ_API_KEY=your_groq_api_key

#Future Enhancements 🔮
📌 Integration with Booking APIs – Enable direct booking of hotels, flights, and activities.
📌 Real-time Weather Updates – Fetch live weather data for travel planning.
📌 User Reviews & Ratings – Collect and display user-generated ratings.
📌 Multi-Language Support – Translate itineraries for global travelers.
