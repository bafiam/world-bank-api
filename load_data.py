import requests
import json

def data_loads():

        # Construct the query
        base_endpoint = "http://api.worldbank.org/v2/"
        method = "/countries" 

        # Configuration
        params = {
                    "format" : "json", # we require the response in json format
                }
        # request the url and store the response in a variable
        try:
            response = requests.get(base_endpoint+method,params=params)
            if response.status_code is not 200:
                return response.status_code
            else:
                get_meta_data=response.json()[0]
                get_all_records=get_meta_data["total"]
            
                # Configuration
                params = {
                            "format" : "json", # we require the response in json format
                            "per_page":get_all_records, # we need to include the additional parameter
                        }
                # request the url and store the response in a variable
                response = requests.get(base_endpoint+method,params=params)
                countries = response.json()[1]
                return countries
        except:
            print("something went wrong when processing the API URL")
            










