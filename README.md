# 🌧️ RainCheck: Will It Rain on My Parade?

**RainCheck** is a web-based prototype that predicts the chances of rainfall at a chosen **location**, **date**, and **time** using real-time weather data from the **OpenWeatherMap API** (or Visual Crossing API).  
It helps event organizers and the public plan outdoor activities by providing **hourly rain probability**, **humidity visualization**, and **forecast recommendations**.

---

## 🚀 Features

- 🔐 **Login Page:** Secure user login before accessing prediction features.
- 📍 **Location Selection:** Choose your desired location on an interactive map.
- 📅 **Date & Time Picker:** Select a specific date and time to check the weather.
- ☔ **Rain Forecast:** Displays rain probability, rainfall amount, and weather condition.
- 💧 **Humidity Visualization:** Graphical representation of hourly humidity trends.
- 📊 **Hourly Charts:** See hourly rainfall probabilities and precipitation data.
- 🛰️ **Future Integration:** Plan to integrate **NASA GPM satellite data** for enhanced accuracy.

---

## 🧠 Future Enhancements

- 🛰️ **Integration of NASA GPM satellite data** for improved rainfall precision.  
- 📈 **Addition of humidity visualization and hourly rain charts** for better data insights.  
- 🤖 **AI-based multi-day rainfall prediction model** using historical data.  
- 🔔 **SMS or Email rain alert notifications** for proactive user updates.  

---

## 🏗️ System Architecture

**Frontend:** React.js  
**Backend:** Python (Flask)  
**APIs Used:** OpenWeatherMap / Visual Crossing  
**Visualization:** Chart.js or Recharts  
**Database (optional):** SQLite / Firebase for user management  

**Workflow:**
1. User logs in via the login page.
2. Enters location, date, and time.
3. Backend sends a request to the weather API.
4. The API returns hourly forecast data.
5. Backend parses rain-related data and calculates rain probability.
6. Results (humidity, chance of rain, forecast) are displayed in charts.

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | React.js |
| Backend | Flask (Python) |
| API | Visual Crossing / OpenWeatherMap |
| Charts | Recharts / Chart.js |
| Styling | CSS / Tailwind |
| Authentication | Flask-Login / Firebase Auth (optional) |

---
