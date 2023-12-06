# import pandas as pd
# import sqlalchemy
# from sqlalchemy import create_engine

# # Read JSON file into a Pandas DataFrame
# json_file_path = '../seeds/recipes-000.json'
# df = pd.read_json(json_file_path, lines=True)

# cnx = create_engine('mysql+pymysql://root:@127.0.0.1/ahmedsharif_test')    
# df.to_sql(con=cnx, name='hellofresh_recipe', if_exists='replace')

# print(f'Data successfully loaded into table.')
