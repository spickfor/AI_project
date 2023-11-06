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


    # while for receiving
    while True:
        # Send an HTTP request to the current page
        response = requests.get(receiving_base_url)

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
                    player_receiving_data_dict[player_info] = {
                        "Player": player_info,
                        "Rec": player_data[1],
                        "Yds": player_data[2],
                        "TD": player_data[3],
                        "20+": player_data[4],
                        "40+": player_data[5],
                        "LNG": player_data[6],
                        "Rec 1st": player_data[7],
                        "1st%": player_data[8],
                        "Rec FUM": player_data[9],
                        "Rec YAC/R": player_data[10],
                        "Tgts": player_data[11]
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
            receiving_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", receiving_base_url)
            break


    # #while for fumbles
    # while True:
    #     # Send an HTTP request to the current page
    #     response = requests.get(fumbles_base_url)

    #     if response.status_code == 200:
    #         html_content = response.text
    #         soup = BeautifulSoup(html_content, 'html.parser')

    #         # Find the <tbody> section to represent the table data
    #         tbody = soup.find('tbody')

    #         if tbody:
    #             # Extract and organize data for each player
    #             for row in tbody.find_all('tr'):
    #                 player_info = row.find('a', class_='d3-o-player-fullname nfl-o-cta--link').get_text(strip=True)
    #                 player_data = [data.get_text(strip=True) for data in row.find_all('td')]
    #                 player_fumbles_data_dict[player_info] = {
    #                     "Player": player_info,
    #                     "FF": player_data[1],
    #                     "FR": player_data[2],
    #                     "FR TD": player_data[3]
    #                 }



    #         # Find the "Next Page" link by searching for the element with class "nfl-o-table-pagination__next"
    #         next_page_link = soup.find('a', {'class': 'nfl-o-table-pagination__next'})

    #         if not next_page_link:
    #             break  # No more pages to scrape

    #         # Get the href attribute of the "Next Page" link
    #         next_page_url = next_page_link.get('href')

    #         if not next_page_url:
    #             break  # No more pages to scrape

    #         # Update the base URL to the URL of the "Next Page" link
    #         fumbles_base_url = f"https://www.nfl.com{next_page_url}"

    #     else:
    #         print("Failed to retrieve data from", fumbles_base_url)
    #         break


    # #while for tackles
    # while True:
    #     # Send an HTTP request to the current page
    #     response = requests.get(tackles_base_url)

    #     if response.status_code == 200:
    #         html_content = response.text
    #         soup = BeautifulSoup(html_content, 'html.parser')

    #         # Find the <tbody> section to represent the table data
    #         tbody = soup.find('tbody')

    #         if tbody:
    #             # Extract and organize data for each player
    #             for row in tbody.find_all('tr'):
    #                 player_info = row.find('a', class_='d3-o-player-fullname nfl-o-cta--link').get_text(strip=True)
    #                 player_data = [data.get_text(strip=True) for data in row.find_all('td')]
    #                 player_tackles_data_dict[player_info] = {
    #                     "Player": player_info,
    #                     "Comb": player_data[1],
    #                     "Asst": player_data[2],
    #                     "Solo": player_data[3],
    #                     "Sck": player_data[4]
    #                 }



    #         # Find the "Next Page" link by searching for the element with class "nfl-o-table-pagination__next"
    #         next_page_link = soup.find('a', {'class': 'nfl-o-table-pagination__next'})

    #         if not next_page_link:
    #             break  # No more pages to scrape

    #         # Get the href attribute of the "Next Page" link
    #         next_page_url = next_page_link.get('href')

    #         if not next_page_url:
    #             break  # No more pages to scrape

    #         # Update the base URL to the URL of the "Next Page" link
    #         tackles_base_url = f"https://www.nfl.com{next_page_url}"

    #     else:
    #         print("Failed to retrieve data from", tackles_base_url)
    #         break


    #while for interceptions
    while True:
        # Send an HTTP request to the current page
        response = requests.get(interceptions_base_url)

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
                    player_interceptions_data_dict[player_info] = {
                        "Player": player_info,
                        "Int": player_data[1],
                        "Int TD": player_data[2],
                        "Int Yds": player_data[3],
                        "Lng": player_data[4]
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
            interceptions_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", interceptions_base_url)
            break



    # while for Field Goals
    while True:
        # Send an HTTP request to the current page
        response = requests.get(field_goal_base_url)

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
                    player_field_goal_data_dict[player_info] = {
                        "Player": player_info,
                        "FGM": player_data[1],
                        "Att": player_data[2],
                        "FG %": player_data[3],
                        "1-19>A-M": player_data[4],
                        "20-29>A-M": player_data[5],
                        "30-39>A-M": player_data[6],
                        "40-49>A-M": player_data[7],
                        "50-59>A-M": player_data[8],
                        "60+>A-M": player_data[9],
                        "LNG": player_data[10],
                        "FG Blk": player_data[11]
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
            field_goal_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", field_goal_base_url)
            break


    # while for kickoffs
    while True:
        # Send an HTTP request to the current page
        response = requests.get(kickoff_base_url)

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
                    player_kickoff_data_dict[player_info] = {
                        "Player": player_info,
                        "KO": player_data[1],
                        "Yds": player_data[2],
                        "Ret Yds": player_data[3],
                        "TB": player_data[4],
                        "TB %": player_data[5],
                        "Ret": player_data[6],
                        "Ret Avg": player_data[7],
                        "OSK": player_data[8],
                        "OSK Rec": player_data[9],
                        "OOB": player_data[10],
                        "TD": player_data[11]
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
            kickoff_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", kickoff_base_url)
            break


    # for kick returns
    while True:
        # Send an HTTP request to the current page
        response = requests.get(kickreturn_base_url)

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
                    player_kickreturn_data_dict[player_info] = {
                        "Player": player_info,
                        "Avg": player_data[1],
                        "Ret": player_data[2],
                        "Yds": player_data[3],
                        "KRet TD": player_data[4],
                        "20+ %": player_data[5],
                        "40+": player_data[6],
                        "LNG": player_data[7],
                        "FC": player_data[8],
                        "FUM": player_data[9]
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
            kickreturn_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", kickreturn_base_url)
            break


    # while for punting
    while True:
        # Send an HTTP request to the current page
        response = requests.get(punting_base_url)

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
                    player_punting_data_dict[player_info] = {
                        "Player": player_info,
                        "Avg": player_data[1],
                        "Net Avg": player_data[2],
                        "Net Yds": player_data[3],
                        "Punts": player_data[4],
                        "LNG": player_data[5],
                        "Yds": player_data[6],
                        "IN 20": player_data[7],
                        "OOB": player_data[8],
                        "DN": player_data[9],
                        "TB": player_data[10],
                        "FC": player_data[11],
                        "Ret": player_data[12],
                        "RetY": player_data[13],
                        "TD": player_data[14],
                        "P Blk": player_data[15]
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
            punting_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", punting_base_url)
            break


    # while for punt returns
    while True:
        # Send an HTTP request to the current page
        response = requests.get(puntreturn_base_url)

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
                    player_puntreturn_data_dict[player_info] = {
                        "Player": player_info,
                        "Avg": player_data[1],
                        "Ret": player_data[2],
                        "Yds": player_data[3],
                        "PRet T": player_data[4],
                        "20+ %": player_data[5],
                        "40+": player_data[6],
                        "LNG": player_data[7],
                        "FC": player_data[8],
                        "FUM": player_data[9]
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
            puntreturn_base_url = f"https://www.nfl.com{next_page_url}"

        else:
            print("Failed to retrieve data from", puntreturn_base_url)
            break


    # conglomerate data into the years
    yearly_passing_player_data_dict[year] = player_passing_data_dict
    yearly_rushing_player_data_dict[year] = player_rushing_data_dict
    yearly_receiving_player_data_dict[year] = player_receiving_data_dict
    yearly_fumbles_player_data_dict[year] = player_fumbles_data_dict
    yearly_tackles_player_data_dict[year] = player_tackles_data_dict
    yearly_interceptions_player_data_dict[year] = player_interceptions_data_dict
    yearly_field_goal_player_data_dict[year] = player_field_goal_data_dict
    yearly_kickoff_player_data_dict[year] = player_kickoff_data_dict
    yearly_kickreturn_player_data_dict[year] = player_kickreturn_data_dict
    yearly_punting_player_data_dict[year] = player_punting_data_dict
    yearly_puntreturn_player_data_dict[year] = player_puntreturn_data_dict





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

        rushing_df.to_excel(writer, sheet_name=f"{year}_Rushing", index=False)

    for year in yearly_receiving_player_data_dict.keys():
        # Convert the receiving player data dictionary to a Pandas DataFrame
        receiving_df = pd.DataFrame(yearly_receiving_player_data_dict[year]).T

        receiving_df.to_excel(writer, sheet_name=f"{year}_Receiving", index=False)

    for year in yearly_fumbles_player_data_dict.keys():
        # Convert the fumbles player data dictionary to a Pandas DataFrame
        fumbles_df = pd.DataFrame(yearly_fumbles_player_data_dict[year]).T

        fumbles_df.to_excel(writer, sheet_name=f"{year}_Fumbles", index=False)

    for year in yearly_tackles_player_data_dict.keys():
        # Convert the tackles player data dictionary to a Pandas DataFrame
        tackles_df = pd.DataFrame(yearly_tackles_player_data_dict[year]).T

        tackles_df.to_excel(writer, sheet_name=f"{year}_Tackles", index=False)

    for year in yearly_interceptions_player_data_dict.keys():
        # Convert the iinterceptinos player data dictionary to a Pandas DataFrame
        interceptions_df = pd.DataFrame(yearly_interceptions_player_data_dict[year]).T

        interceptions_df.to_excel(writer, sheet_name=f"{year}_Interceptions", index=False)

    for year in yearly_field_goal_player_data_dict.keys():
        # Convert the field goal player data dictionary to a Pandas DataFrame
        field_goal_df = pd.DataFrame(yearly_field_goal_player_data_dict[year]).T

        field_goal_df.to_excel(writer, sheet_name=f"{year}_Field Goal", index=False)

    for year in yearly_kickoff_player_data_dict.keys():
        # Convert the Kickoff player data dictionary to a Pandas DataFrame
        kickoff_df = pd.DataFrame(yearly_kickoff_player_data_dict[year]).T

        kickoff_df.to_excel(writer, sheet_name=f"{year}_Kickoff", index=False)

    for year in yearly_kickreturn_player_data_dict.keys():
        # Convert the Kick return player data dictionary to a Pandas DataFrame
        kickreturn_df = pd.DataFrame(yearly_kickreturn_player_data_dict[year]).T

        kickreturn_df.to_excel(writer, sheet_name=f"{year}_Kick Return", index=False)

    for year in yearly_punting_player_data_dict.keys():
        # Convert the puntplayer data dictionary to a Pandas DataFrame
        punting_df = pd.DataFrame(yearly_punting_player_data_dict[year]).T

        punting_df.to_excel(writer, sheet_name=f"{year}_Punting", index=False)

    for year in yearly_puntreturn_player_data_dict.keys():
        # Convert the Kick return player data dictionary to a Pandas DataFrame
        puntreturn_df = pd.DataFrame(yearly_puntreturn_player_data_dict[year]).T

        puntreturn_df.to_excel(writer, sheet_name=f"{year}Punt Return", index=False)


print("Data saved to player_data.xlsx")
