# import module
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class Extract:

    def __init__(self):
        self._df_time = None
        self._df_seasons = None
        self._df_teams = None

    def extract(self):
        driver = webdriver.Chrome('/chromedriver')

        team_name_list = []
        years_list = []
        total_wins_list = []
        total_losses_list = []
        total_ot_losses_list = []
        goals_for_list = []
        goals_against_list = []

        for i in range(1, 7):
            driver.get(f"https://www.scrapethissite.com/pages/forms/?page_num={i}&per_page=100")

            teams_name = driver.find_elements(By.CLASS_NAME, "name")
            years = driver.find_elements(By.CLASS_NAME, "year")
            total_wins = driver.find_elements(By.CLASS_NAME, "wins")
            total_losses = driver.find_elements(By.CLASS_NAME, "losses")
            total_ot_losses = driver.find_elements(By.CLASS_NAME, "ot-losses")
            goals_for = driver.find_elements(By.CLASS_NAME, "gf")
            goals_against = driver.find_elements(By.CLASS_NAME, "ga")

            for j in range(len(teams_name)):
                team_name_list.append(teams_name[j].text)
                years_list.append(years[j].text)
                total_wins_list.append(total_wins[j].text)
                total_losses_list.append(total_losses[j].text)
                total_ot_losses_list.append(total_ot_losses[j].text)
                goals_for_list.append(goals_for[j].text)
                goals_against_list.append(goals_against[j].text)

        self._df_seasons = pd.DataFrame({'team_name': team_name_list,
                                         'year': years_list,
                                         'total_wins': total_wins_list,
                                         'total_losses': total_losses_list,
                                         'total_overtime_losses': total_ot_losses_list,
                                         'goals_for': goals_for_list,
                                         'goals_against': goals_against_list})

        self._df_time = pd.DataFrame({'year': years_list})

        self._df_teams = pd.DataFrame({'name': team_name_list})

    def get_df_time(self):
        return self._df_time

    def get_df_seasons(self):
        return self._df_seasons

    def get_df_teams(self):
        return self._df_teams
