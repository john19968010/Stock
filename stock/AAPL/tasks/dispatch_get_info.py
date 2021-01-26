from celery.decorators import task
import yfinance as yf
import json
from AAPL.models import AAPL


@task(name="get_aapl_info")
def get_aapl_info(day):
    current_date = f"{day.year}-{day.month}-{day.day}"
    data = yf.download("AAPL", start=current_date, end=current_date)
    dict1 = data.to_dict(orient="index")

    stock = {
        "date" : day,
        "high" : "",
        "low" :"",
        "open": "",
        "close": ""
    }
    # stock["date"] = 
    for key, value in dict1.items():
        element1 = []
        element1.append(date)
        element1.append(round(value["Open"],1 ))
        element1.append(round(value["Adj Close"],1 ))
        element1.append(round(value["Low"],1 ))
        element1.append(round(value["High"],1 ))
        stock.append(element1)
    return stock