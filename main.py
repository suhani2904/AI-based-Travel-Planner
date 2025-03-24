from flask import Flask, jsonify, render_template , request
from find_places import find_places_stored_in_neo4j
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/places' , methods = ['POST' , 'GET'])
def places():
    if request.method == 'POST':
        destination = request.form.get('destination')
        days = request.form.get('days')
        preferences = request.form.getlist('preferences')
        budget = request.form.get('budget')
        places_list = find_places_stored_in_neo4j(destination , preferences , days , budget)
        return render_template('places_list.html' , destination = destination , places_list = places_list)
        
if __name__=="__main__":
    app.run(debug=True)

