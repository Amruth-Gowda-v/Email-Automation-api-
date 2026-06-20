from smtplib import *
import requests
import json

my_email=""
my_pass=""
yor_email=""


api_key="DQNOOLVUUYPRAUNL"
api=api = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={api_key}"
response = requests.get(api)
response.raise_for_status()
stocks = response.json()

with open("stocks.json", "w") as file:
    json.dump(stocks, file, indent=4)

with open("stocks.json", "r") as file:
    data = json.load(file)
    quote = data["Global Quote"]

symbol = quote["01. symbol"]
open_price = quote["02. open"]
high_price = quote["03. high"]
low_price = quote["04. low"]
change_percent = quote["10. change percent"]


with SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs=yor_email,msg = f"""Subject: IBM Stock Report

Symbol: {symbol}
Open: {open_price}
High: {high_price}
Low: {low_price}
change percent: {change_percent}
""")


print("Email sent successfully!")



