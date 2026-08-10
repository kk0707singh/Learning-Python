import pandas as pd

# from io import StringIO
# Data = '{"employee_name": "james", "email": "james@gmail.com", "job_profile": [{"title1": "team_lead", "title2": "sde"}]}'
# df = pd.read_json(StringIO(Data)) 
# print(df)

# # convert back into json:
# print(df.to_json())

# print(df.to_json(orient='index'))
# print(df.to_json(orient='records'))


# # reading csv file through url:
# df = pd.read_csv("url_link", header=None)

# # convert back into csv file:
# df.to_csv("csvlink")

# reading html

# url = 'https://www.fdic.gov/bank-failures/failed-bank-list'
# df = pd.read_html(url)
# print(df[0])

df = pd.read_excel('Chapter-16-Reading-data-using-pandas/data.xlsx')
print(df )
df.to_pickle('df')
# how to read pickle file:
pd.read_pickle('df')