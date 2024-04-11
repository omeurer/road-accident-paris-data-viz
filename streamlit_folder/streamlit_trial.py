import requests
import pandas as pd

# URL of the JSON file on GitHub
url = 'https://raw.githubusercontent.com/omeurer/road-accident-paris-data-viz/streamlit-try/data/full_data.json'
# Fetch the JSON file from the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data
    data = response.json()

    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)

    # Now you have your DataFrame
    print(df)
else:
    print('Failed to fetch data from GitHub:', response.status_code)