# Weather ETL Pipeline 🌤️

A Python-based ETL (Extract, Transform, Load) pipeline that fetches real-time weather data for multiple Indian cities using the OpenWeatherMap API, transforms it, and stores it in a SQLite database.

## 🏙️ Cities Tracked
- Jaipur, Rajasthan
- Delhi, NCR
- Mumbai, Maharashtra

## 🛠️ Tech Stack
- Python 3.13
- Pandas (data transformation)
- SQLite (data storage)
- OpenWeatherMap REST API
- python-dotenv (secure API key management)

## ⚙️ ETL Pipeline Flow
Extract → Transform → Load
OpenWeatherMap API → Pandas (Kelvin to Celsius, column selection) → SQLite DB

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Create a `.env` file in the root folder:
   api-token=your_openweathermap_api_key
4. Run the pipeline:
   cd src
   python main.py --frequency 600

## 📦 Features
- Fetches live weather data every N seconds (configurable)
- Transforms temperature from Kelvin to Celsius
- Prevents duplicate entries in the database
- Logs all pipeline activity with timestamps
- Error handling for API failures

## 📊 Database Schema
| Column     | Type    | Description                  |
|------------|---------|------------------------------|
| dt         | INTEGER | Unix timestamp (primary index)|
| temp       | REAL    | Temperature in Celsius        |
| temp_min   | REAL    | Min temperature               |
| temp_max   | REAL    | Max temperature               |
| pressure   | INTEGER | Atmospheric pressure          |
| humidity   | INTEGER | Humidity percentage           |
| wind_speed | REAL    | Wind speed m/s                |
| wind_deg   | INTEGER | Wind direction degrees        |
| name       | TEXT    | City name                     |