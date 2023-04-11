class Load:
    def __init__(self, df_time, df_teams, df_seasons, connection):
        self._df_time = df_time
        self._df_teams = df_teams
        self._df_seasons = df_seasons
        self._connection = connection

    def __load_time_table(self):
        for row in self._df_time.to_numpy():
            query = 'INSERT INTO time(year) VALUES (%s)' % (row[0])
            self._connection.execute(query)

    def __load_teams_table(self):
        for row in self._df_teams.to_numpy():
            query = 'INSERT INTO teams(name) VALUES (\'%s\')' % (row[0])
            self._connection.execute(query)

    def __load_seasons_table(self):
        for row in self._df_seasons.to_numpy():
            query = 'INSERT INTO seasons(team_name, year, total_wins, total_losses, total_overtime_losses, ' \
                    'percentage_wins, goals_for, goals_against, goals_difference) VALUES (\'%s\', %s, %s, %s, %s, ' \
                    '%s, %s, %s, %s)' % (row[0], row[1], row[2], row[3], row[4], row[7], row[5], row[6], row[8])
            self._connection.execute(query)

    def load(self):
        self.__load_time_table()
        self.__load_teams_table()
        self.__load_seasons_table()
