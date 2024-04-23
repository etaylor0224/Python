class NotificationManager:
    def __init__(self, result):
        fly_from = result["cityFrom"]
        fly_from_code = result["cityCodeFrom"]
        fly_to = result["cityTo"]
        fly_to_code = result["cityCodeTo"]
        fly_date = result["local_departure"]
        fly_cost = result["price"]

        print(f"Low price alert! Only ${fly_cost} to fly from {fly_from}-{fly_from_code} to {fly_to}-{fly_to_code} "
              f"leaving on {fly_date}. ")
    #This class is responsible for sending notifications with the deal flight details.