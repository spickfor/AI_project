#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

start_year = 2022
current_year = 2023


# outer dict to hold data by year
yearly_passing_player_data_dict = {}
yearly_rushing_player_data_dict = {}
yearly_receiving_player_data_dict = {}
yearly_fumbles_player_data_dict = {}
yearly_tackles_player_data_dict = {}
yearly_interceptions_player_data_dict = {}
yearly_field_goal_player_data_dict = {}
yearly_kickoff_player_data_dict = {}
yearly_kickreturn_player_data_dict = {}
yearly_punting_player_data_dict = {}
yearly_puntreturn_player_data_dict = {}

for year in range(start_year, current_year + 1):

    # Set the base URL for the player passing stats
    passing_base_url = f"https://www.nfl.com/stats/player-stats/category/passing/{year}/REG/all/passingyards/DESC"
    
    rushing_base_url = f"https://www.nfl.com/stats/player-stats/category/rushing/{year}/reg/all/rushingyards/desc"

    receiving_base_url = f"https://www.nfl.com/stats/player-stats/category/receiving/{year}/reg/all/receivingreceptions/desc"

    fumbles_base_url = f"https://www.nfl.com/stats/player-stats/category/fumbles/{year}/reg/all/defensiveforcedfumble/desc"

    tackles_base_url = f"https://www.nfl.com/stats/player-stats/category/tackles/{year}/reg/all/defensivecombinetackles/desc"

    interceptions_base_url = f"https://www.nfl.com/stats/player-stats/category/interceptions/{year}/reg/all/defensiveinterceptions/desc"

    field_goal_base_url = f"https://www.nfl.com/stats/player-stats/category/field-goals/{year}/reg/all/kickingfgmade/desc"

    kickoff_base_url = f"https://www.nfl.com/stats/player-stats/category/kickoffs/{year}/reg/all/kickofftotal/desc"

    kickreturn_base_url = f"https://www.nfl.com/stats/player-stats/category/kickoff-returns/{year}/reg/all/kickreturnsaverageyards/desc"

    punting_base_url = f"https://www.nfl.com/stats/player-stats/category/punts/{year}/reg/all/puntingaverageyards/desc"

    puntreturn_base_url = f"https://www.nfl.com/stats/player-stats/category/punt-returns/({year})/reg/all/puntreturnsaverageyards/desc"



    # Initialize a dictionary to hold player data
    player_passing_data_dict = {}
    player_rushing_data_dict = {}
    player_receiving_data_dict = {}
    player_fumbles_data_dict = {}
    player_tackles_data_dict = {}
    player_interceptions_data_dict = {}
    player_field_goal_data_dict = {}
    player_kickoff_data_dict = {}
    player_kickreturn_data_dict = {}
    player_punting_data_dict = {}
    player_puntreturn_data_dict = {}

    # for passing
    while True:
        # Send an HTTP request to the current page
        response = requests.get(passing_base_url)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the <tbody> section to represent the table data
            tbody = soup.find('tbody')

            if tbody:
                # Extract and organize data for each player
                for row in tbody.find_all('tr'):
                    player_info = row.find('a', class_='d3-o-player-fullname nfl-o-cta--link').get_text(strip=True)
                    player_data = [data.get_text(strip=True) for data in row.find_all('td')]
                    player_passing_data_dict[player_info] = {
                        "Player": player_info,
                        "Pass Yds": player_data[1],
                        "Yds/Att": player_data[2],
                        "Att": player_data[3],
                        "Cmp": player_data[4],
                        "Cmp %": player_data[5],
                        "TD": player_data[6],
                        "INT": player_data[7],
                        "Rate": player_data[8],
                        "1st": player_data[9],
                        "1st%": player_data[10],
                        "20+": player_data[11],
                        "40+": player_data[12],
                        "Lng": player_data[13],
                        "Sck": player_data[14],
                        "SckY": player_data[15]
                    }


            # Find the "Next Page" link by searching for the element with class "nfl-o-table-pagination__next"
            next_page_link = soup.find('a', {'class': 'nfl-o-table-pagination__next'})

            if not next_page_link:
                break  # No more pages to scrape

            # Get the href attribute of the "Next Page" link
            next_page_url = next_page_link.get('href')

            if not next_page_url:
                break  # No more pages to scrape

            # Update the base URL to the URL of the "Next Page" link
            passing_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", passing_base_url)
            break


    # for rushing
    while True:
        # Send an HTTP request to the current page
        response = requests.get(rushing_base_url)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the <tbody> section to represent the table data
            tbody = soup.find('tbody')

            if tbody:
                # Extract and organize data for each player
                for row in tbody.find_all('tr'):
                    player_info = row.find('a', class_='d3-o-player-fullname nfl-o-cta--link').get_text(strip=True)
                    player_data = [data.get_text(strip=True) for data in row.find_all('td')]
                    player_rushing_data_dict[player_info] = {
                        "Player": player_info,
                        "Rush Yds": player_data[1],
                        "Att": player_data[2],
                        "TD": player_data[3],
                        "20+": player_data[4],
                        "40+": player_data[5],
                        "Lng": player_data[6],
                        "Rush 1st": player_data[7],
                        "Rush 1st%": player_data[8],
                        "Rush FUM": player_data[9]
                    }

                # for testing
                

            # Find the "Next Page" link by searching for the element with class "nfl-o-table-pagination__next"
            next_page_link = soup.find('a', {'class': 'nfl-o-table-pagination__next'})

            if not next_page_link:
                break  # No more pages to scrape

            # Get the href attribute of the "Next Page" link
            next_page_url = next_page_link.get('href')

            if not next_page_url:
                break  # No more pages to scrape

            # Update the base URL to the URL of the "Next Page" link
            rushing_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", rushing_base_url)
            break



    # conglomerate data into the years
    yearly_passing_player_data_dict[year] = player_passing_data_dict
    yearly_rushing_player_data_dict[year] = player_rushing_data_dict


# for player, data in yearly_rushing_player_data_dict[2023].items():
#     print(player)
#     for column, value in data.items():
#         print(f"{column}: {value}")
#     print("\n")



# Initialize a Pandas Excel writer
with pd.ExcelWriter('player_data.xlsx', engine='openpyxl', mode='w') as writer:
    for year in yearly_passing_player_data_dict.keys():
        # Convert the passing player data dictionary to a Pandas DataFrame
        passing_df = pd.DataFrame(yearly_passing_player_data_dict[year]).T

        # Write the passing DataFrame to the Excel sheet with the year as the sheet name
        passing_df.to_excel(writer, sheet_name=f"{year}_Passing", index=False)

    for year in yearly_rushing_player_data_dict.keys():
        # Convert the rushing player data dictionary to a Pandas DataFrame
        rushing_df = pd.DataFrame(yearly_rushing_player_data_dict[year]).T

        # Write the rushing DataFrame to the Excel sheet with the year as the sheet name
        rushing_df.to_excel(writer, sheet_name=f"{year}_Rushing", index=False)

print("Data saved to player_data.xlsx")
