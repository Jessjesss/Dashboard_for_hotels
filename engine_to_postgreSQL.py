import pandas as pd
from sqlalchemy import create_engine


try:
    con = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/postgres')
except:
    print("Can't create 'engine")

df = pd.read_csv('C:/Users/Jess/pet_project/sales_fact.csv')
df.to_sql('sales_fact', con, 'hotels', index=False,if_exists='replace',method='multi')

