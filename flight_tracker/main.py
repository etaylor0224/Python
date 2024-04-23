from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


flightdata = FlightData()


for loc in flightdata.flight_code:
    search = FlightSearch(loc)
    search_result = search.output
    results = search_result["data"]

    budget = flightdata.flight_df[flightdata.flight_df["IATA Code"] == loc]
    budget_price = budget["Lowest Price"].item()

    for x in range(len(results)):
        cost = results[x]["price"]
        if cost < budget_price:
            low = results[x]
            NotificationManager(low)
