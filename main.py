from Connection import Connection
from Extract import Extract
from Transform import Transform



extract = Extract()
extract.extract()
print(extract.get_df_seasons().iloc[0])
#connection = Connection()



