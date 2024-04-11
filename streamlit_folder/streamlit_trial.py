import requests

# URL of the JSON file on GitHub
url = 'https://raw.githubusercontent.com/yourusername/yourrepository/master/yourfile.json'

# Fetch the JSON file from the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the JSON data
    data = response.json()

    # Now you have your JSON data and can process it as needed
    print(data)
else:
    print('Failed to fetch data from GitHub:', response.status_code)