class PurpleAirAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.purpleair.com/v1/"
        self.api_key = api_key

    def func_name(fields: list, 