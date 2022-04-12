import requests
# Enter your Sheety endpoint prices
SHEET_ENDPOINT = "enter your api"
# Enter your Sheety endpoint users
SHEET_ENDPOINT_USERS = "enter your api"


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}",json=new_data)
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(SHEET_ENDPOINT_USERS)
        data = response.json()
        self.customer_data = data["users"]

        return self.customer_data
