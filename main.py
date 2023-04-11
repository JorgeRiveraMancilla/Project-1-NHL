from Connection import Connection
from Load import Load
from Transform import Transform
from Extract import Extract

connection = Connection()

with open('scripts/star_schema.sql', 'r') as file:
    for line in file.read().split(';'):
        connection.execute(line)

extract = Extract()
extract.extract()

transform = Transform(extract.get_df_time(), extract.get_df_teams(), extract.get_df_seasons())
transform.transform()

load = Load(transform.get_df_time(), transform.get_df_teams(), transform.get_df_seasons(), connection)
load.load()
