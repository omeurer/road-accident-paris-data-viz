import requests
import pandas as pd

# API endpoint URL
url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/accidentologie0/records?limit=20"

# Parameters for the API request
# Sending GET request to the API
params = {
    'disjunctive.com_arm_code': True,
    'disjunctive.victime_type': True,
    'disjunctive.gravite': True,
    'disjunctive.tranche_age_victime': True,
    'sort': '-com_arm_code',
    'format': 'json'
}


def get_dataframe():
    # Sending GET request to the API
    response = requests.get(url, params=params)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Load JSON response into a pandas DataFrame
        data = response.json()
        if 'results' in data:
            df = pd.json_normalize(data['results'])

        else:
            print("No records found in the JSON response.")
    else:
        print("Error occurred while downloading data. Status code:", response.status_code)

    return df
