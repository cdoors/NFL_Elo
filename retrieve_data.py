import pandas as pd
import requests
from bs4 import BeautifulSoup

def main():
    """
    Main function to retrieve NFL game data and save to CSV.
    """
    data = retrieve_nfl_data()
    if data is not None:
        save_data_to_csv(data, "nfl_scores.csv")
        print("Data has been successfully retrieved and saved to nfl_scores.csv")
    else:
        print("No data to save. Data retrieval failed.")

def retrieve_nfl_data():
    """
    Retrieve NFL game data by scraping from footballdb.com.
    
    Returns:
    pandas.DataFrame: DataFrame containing NFL game data
    """
    try:
        url = "https://www.footballdb.com/games/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        data = []
        table = soup.find('table', class_='statistics')
        rows = table.find_all('tr')[1:]  # Skip header row
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:
                date = cols[0].text.strip()
                away_team = cols[1].text.strip()
                away_score = cols[2].text.strip()
                home_team = cols[3].text.strip()
                home_score = cols[4].text.strip()
                data.append([date, away_team, away_score, home_team, home_score])
        
        df = pd.DataFrame(data, columns=['Date', 'Away Team', 'Away Score', 'Home Team', 'Home Score'])
        return df
    except Exception as e:
        print(f"Failed to retrieve NFL data: {str(e)}")
        return None

def save_data_to_csv(data, filename):
    """
    Save the retrieved data to a CSV file.
    
    Args:
    data (pandas.DataFrame): DataFrame to save
    filename (str): Name of the CSV file
    """
    try:
        data.to_csv(filename, index=False)
    except Exception as e:
        print(f"Failed to save data to CSV: {str(e)}")

if __name__ == "__main__":
    main()
