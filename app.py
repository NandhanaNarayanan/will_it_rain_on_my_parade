from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)  # <-- corrected here
CORS(app)  # Allow frontend to access backend

API_KEY = "FCBLT7F95ZB5SSNHYWUWGPR2X"  # Your Visual Crossing API key

@app.route('/api/rain', methods=['GET'])
def rain_forecast():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    date_str = request.args.get('date')

    if not lat or not lon or not date_str:
        return jsonify({"error": "Missing latitude, longitude, or date"}), 400

    try:
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}/{date_str}?unitGroup=metric&key={API_KEY}&include=hours"
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch weather data"}), 500

        data = response.json()
        hours = data.get("days", [])[0].get("hours", [])

        rain_hours = [h for h in hours if "rain" in h.get("conditions", "").lower()]
        probability_percent = round((len(rain_hours) / len(hours)) * 100, 2) if hours else 0
        forecast_rain_mm = round(sum(h.get("precip", 0) for h in hours), 2)

        result = {
            "date": date_str,
            "forecast_rain_mm": forecast_rain_mm,
            "probability_percent": probability_percent
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':  # <-- corrected here
    app.run(debug=True)
