from pycoingecko import CoinGeckoAPI
import asyncio
from bscscan import BscScan
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
cg = CoinGeckoAPI()
from requests_html import HTMLSession

def get_top_coins_across_categories():
    
    categories_with_market_data = cg.get_coins_categories()   
    unique_list = {}
    for row in categories_with_market_data:
        for row_3 in row["top_3_coins"]:
            if row_3 not in unique_list:
                unique_list[row_3] = 1
            else:
                unique_list[row_3] = unique_list[row_3] + 1
        #     unique_list[row["top_3_coins"]] = 1

    sorted_x = sorted(unique_list.items(), key=lambda kv: kv[1],reverse=True)
    for row in sorted_x:
        print(row)

# YOUR_API_KEY = "HX4AXDENIGU12MTUUIN654EBVDHG6P2XV4"

# async def main():
#   async with BscScan(YOUR_API_KEY) as bsc:
#     print(await bsc.get_bnb_balance(address="0x0000000000000000000000000000000000001004"))

# if __name__ == "__main__":
#   asyncio.run(main())

import csv
import requests

CSV_URL = 'https://bscscan.com/exportData?type=tokenholders&contract=0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d&decimal=18'


with requests.Session() as s:
    download = s.get(CSV_URL)
    count = 0
    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    while count < 1:
        for row in my_list:
            print(row)
            count = count + 1