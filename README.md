**AI-Based Travel Planner** 🌍✈️



***Overview***<br>
The AI-Based Travel Planner is an intelligent travel assistant that helps users create personalized travel itineraries based on their source, destination, number of days, budget, and preferences. The system integrates LangChain for intelligent query processing, Neo4j for graph-based data storage, and Retrieval-Augmented Generation (RAG) for efficient search. If requested places are not found in Neo4j, the system dynamically fetches LLM-generated insights, Wikipedia descriptions, and images before storing them for future use.

***Features*** 🚀<br>
✅ User-Centric Itinerary Generation – Users enter their destination, budget, duration, and preferences, and the system generates an optimized itinerary.<br>
✅ AI-Powered Recommendations – The planner suggests historical places, parks, food spots, adventure activities, and more based on user preferences.<br>
✅ RAG-Based Search with Neo4j & LangChain – If places exist in the database, results are fetched quickly; otherwise, new places are retrieved, processed, and stored.<br>
✅ Multi-Source Data Retrieval – The system fetches Wikipedia for descriptions & images, LLM (via LangChain) for structured data, and Google search if needed.<br>
✅ Ticket Price & Rating Estimation – The system intelligently estimates ticket prices and ratings for places.<br>
✅ Interactive Web UI – Built using Flask, HTML, CSS, and JavaScript, with clickable place cards that reveal more details like detail description , rating , ticket price on click.<br>

***Tech Stack*** 🛠️<br>
🔹 Backend: Flask, Neo4j, Python, LangChain<br>
🔹 Frontend: HTML, CSS, JavaScript<br>
🔹 Database: Neo4j (Graph Database)<br>
🔹 AI & ML: LangChain, Retrieval-Augmented Generation (RAG), LLM (Language Model for text processing), Wikipedia API<br>

***Project Workflow*** 🛠️<br>
1️⃣ User Input: The user provides a destination, number of days, budget, and preferences.<br>
2️⃣ RAG Search with LangChain & Neo4j: If data exists, fetch and display results instantly.<br>
3️⃣ Data Retrieval: If missing, fetch places via LLM search (LangChain), Wikipedia, and Google search.<br>
4️⃣ Wikipedia API: Extract descriptions and images for the places.<br>
5️⃣ LangChain Processing: Generate ticket prices, ratings, and category-based recommendations.<br>
6️⃣ Store in Neo4j: Save new places for future use.<br>
7️⃣ Display Results: Show the travel itinerary in a structured and visually appealing format.<br>

***Installation & Setup*** 🛠️<br>
1️⃣ Clone the Repository<br>
```
git clone https://github.com/yourusername/AI-Travel-Planner.git
```
cd AI-Travel-Planner
2️⃣ Install Dependencies<br>
```
pip install -r requirements.txt
```
3️⃣ Set Up Environment Variables<br>
Create a .env file and add:<br>
```
NEO4J_URI=your_neo4j_uri<br>
NEO4J_USERNAME=your_neo4j_username<br>
NEO4J_PASSWORD=your_neo4j_password<br>
GROQ_API_KEY=your_groq_api_key<br>
```
4️⃣ Run the Flask App<br>
```
python main.py
```
Access the app at http://127.0.0.1:5000/ 🌍

***Future Enhancements*** 🔮<br>
📌 Integration with Booking APIs – Enable direct booking of hotels, flights, and activities.<br>
📌 Real-time Weather Updates – Fetch live weather data for travel planning.<br>
📌 User Reviews & Ratings – Collect and display user-generated ratings.<br>
📌 Multi-Language Support – Translate itineraries for global travelers.<br>

***Contributing*** 🤝<br>
Feel free to fork this repo, open issues, and submit pull requests. Contributions are always welcome!
