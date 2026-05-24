from create_db import create_DB_connection, close_connection
from create_pandas_df_from_json import convert_dict_to_df
from update_db import update_db
from transform import keep_columns, change_col_name, convert_kelvin_to_celsius, set_datetime_col_as_row_index
from get_weather_data_from_OpenWeatherMap import get_current_weather_data_from_OpenWeatherMap, write_weather_data_in_json_file
import argparse
import time
import logging

# Setup logging
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

CITY_IDS = {
    "Jaipur": "1269515",
    "Delhi": "1273294",
    "Mumbai": "1275339"
}

parser = argparse.ArgumentParser()
parser.add_argument("--frequency", default=600, type=int, help="How often does the program run in seconds")
args = parser.parse_args()

def start():
    for city_name, city_id in CITY_IDS.items():
        try:
            print(f"Fetching weather data for {city_name}...")
            logging.info(f"Fetching weather data for {city_name}")
            returned_connection = create_DB_connection()
            filename = write_weather_data_in_json_file(
                get_current_weather_data_from_OpenWeatherMap(city_id))
            new_df_to_sql = set_datetime_col_as_row_index(convert_kelvin_to_celsius(
                change_col_name(keep_columns(convert_dict_to_df(filename)))))
            update_db(new_df_to_sql, returned_connection)
            close_connection(returned_connection)
            logging.info(f"Successfully processed {city_name}")
        except Exception as e:
            print(f"Error fetching data for {city_name}: {e}")
            logging.error(f"Error fetching data for {city_name}: {e}")

print("Pipeline started. Fetching weather data for Jaipur, Delhi, Mumbai...")
while True:
    start()
    print(f"Waiting {args.frequency} seconds before next run...")
    time.sleep(args.frequency)
