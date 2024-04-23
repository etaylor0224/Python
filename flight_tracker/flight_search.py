import requests
import datetime as dt

class FlightSearch:

    def __init__(self, fly_loc):
        flight_api_key = APIKEY
        kiwi_url = "https://api.tequila.kiwi.com/v2/search"
        fly_from = "LHR"
        fly_to = fly_loc
        datefrom = dt.datetime.today().strftime("%d/%m/%Y")
        six_months = dt.datetime.today().replace(month=(dt.datetime.today().month+6))
        dateto = six_months.strftime("%d/%m/%Y")


        kiwi_headers = {
            "apikey": flight_api_key,
            "Content-Type": "application/json",
            "Content-Encoding": "gzip"
        }
        kiwi_params = {
            "fly_to": fly_to,
            "fly_from": fly_from,
            "date_to": dateto,
            "date_from": datefrom,
            "adults": "1",
            "curr": "EUR",
        }
        self.kiwi_request = requests.get(url=kiwi_url, params=kiwi_params, headers=kiwi_headers)
        self.kiwi_request.raise_for_status()
        self.output = self.kiwi_request.json()
    #This class is responsible for talking to the Flight Search API.