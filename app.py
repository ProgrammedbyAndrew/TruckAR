from flask import Flask, jsonify, render_template, request
from geopy.distance import geodesic

app = Flask(__name__)

# Food truck location
food_truck_location = {"name": "Taco Truck", "lat": 37.7749, "lng": -122.4194}

@app.route('/')
def home():
    return render_template('index.html', truck=food_truck_location)

@app.route('/distance', methods=['GET'])
def calculate_distance():
    # Get user location from query parameters
    user_lat = float(request.args.get('lat'))
    user_lng = float(request.args.get('lng'))
    user_location = (user_lat, user_lng)

    # Calculate distance and bearing
    truck_location = (food_truck_location["lat"], food_truck_location["lng"])
    distance = geodesic(user_location, truck_location).meters

    return jsonify({
        "name": food_truck_location["name"],
        "distance": f"{distance:.2f} meters",
        "lat": food_truck_location["lat"],
        "lng": food_truck_location["lng"]
    })

if __name__ == "__main__":
    app.run(debug=True)