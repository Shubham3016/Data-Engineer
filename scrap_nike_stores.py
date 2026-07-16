import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Premier League table
url = "https://www.bbc.com/sport/football/premier-league/table"

# Add headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing the Premier League data
    table = soup.find('table', {'class': 'gs-o-table'})
    
    if table is None:
        print("Table not found on the webpage.")
        exit()
    
    # Extract table headers
    headers = [header.text.strip() for header in table.find_all('th')]
    
    # Extract table rows
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all(['th', 'td'])
        rows.append([cell.text.strip() for cell in cells])
    
    # Create a DataFrame using pandas
    df = pd.DataFrame(rows, columns=headers)
    
    # Display the DataFrame
    print(df)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")