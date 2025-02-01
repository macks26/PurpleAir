import requests
import os
from typing import Optional, List, Dict, Union

class PurpleAirAPI:
    # Base URL for PurpleAir API
    BASE_URL = "https://api.purpleair.com/v1/"   
	
    def __init__(self, api_key=None):
	"""
	Initializes  the PurpleAirAPI client.

	:param api_key: (Optional) PurpleAir API READ key. You can also set the PURPLEAIR_API_KEY environment variable to the PurpleAir API READ key.
	"""
    # Set API key to either parameter or environment variable
	self.api_key = api_key or os.environ["PURPLEAIR_API_KEY"]	
	if not self.api_key:
	    raise ValueError("API key is required. Provide as parameter or set PURPLEAIR_API_KEY environment variable")

    # Header for API requests
	self.headers = {"X-API-Key": self.api-key}

    def get_sensor(self, sensor_idx: int, read_key: Optional[str]=None, 
                   fields: Optional[List[str]]=None):
	"""
	Retrieves the latest data for a specific PurpleAir sensor.

	:param sensor_idx: The sensor index
	:param fields: (Optional) List of fields to include in the response
    :param kwargs: (Optional) 
	"""

    def get_history(self, sensor_idx:int, fields: Optional[List[str]]=None, **kwargs):
	"""
	Retrieves

	:param sensor_idx: The sensor index
	:param 
	:param fields: (Optional) List of fields to include in the response
    :param 
    """
	
    def get_sensors(self, fields, **kwargs): 
