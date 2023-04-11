class Transform:
    def __init__(self, df_time, df_teams, df_seasons):
        self._df_time = df_time
        self._df_teams = df_teams
        self._df_seasons = df_seasons

    def __generate_percentage_wins(self):
        self._df_seasons['percentage_wins'] = round(self._df_seasons['total_wins'] / (self._df_seasons['total_wins'] +
                                                                                      self._df_seasons['total_losses'] +
                                                                                      self._df_seasons[
                                                                                          'total_overtime_losses']),
                                                    ndigits=3)

    def __generate_goals_difference(self):
        self._df_seasons['goals_difference'] = self._df_seasons['goals_for'] - self._df_seasons['goals_against']

    def __group_equal_row(self):
        self._df_time.drop_duplicates(inplace=True)
        self._df_teams.drop_duplicates(inplace=True)

    def transform(self):
        self.__generate_percentage_wins()
        self.__generate_goals_difference()
        self.__group_equal_row()

    def get_df_time(self):
        return self._df_time

    def get_df_seasons(self):
        return self._df_seasons

    def get_df_teams(self):
        return self._df_teams
