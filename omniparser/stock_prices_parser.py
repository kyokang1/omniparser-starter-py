
# stock_prices_parser.py

import os
import statistics
import pandas
import json

def calculate_latest_closing_price_from_json(x):
    #breakpoint()   # breakpoint is inside def so it will not be get to here unless the main code invoke the defined function
#    return "HEY!!"

    with open(x, "r") as f:
        file_contents = f.read()
    #    print(type(file_contents)) #> str

    aapl = json.loads(file_contents)
    
    meta = aapl["Meta Data"]
    last_refreshed = meta["3. Last Refreshed"]
    
    daily = aapl["Time Series (Daily)"]
    latest_data = daily[str(last_refreshed)]
    latest_closing_price = latest_data["4. close"]

    return latest_closing_price
 

if __name__ == "__main__":

    print("PARSING SOME STOCK PRICES HERE...")
    aapl_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_aapl.json")
    aapl_price = calculate_latest_closing_price_from_json(aapl_filepath)
    print(aapl_price)


