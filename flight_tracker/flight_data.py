import pandas as pd

class FlightData:

    def __init__(self):
        self.flight_df = pd.read_excel("flight_deals.xlsx")
        self.flight_code = [code for code in self.flight_df["IATA Code"]]
    #This class is responsible for structuring the flight data.