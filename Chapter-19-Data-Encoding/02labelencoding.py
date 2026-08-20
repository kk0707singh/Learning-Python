import pandas as pd
from sklearn.preprocessing import LabelEncoder

# create a simple dataframe:
df = pd.DataFrame({
    'color':['red', 'blue', 'green', 'green', 'red', 'blue']
})
print(df.head())

lbl_encoder = LabelEncoder()
print(lbl_encoder.fit_transform(df[['color']]))
print(lbl_encoder.transform([['red']]))
print(lbl_encoder.transform([['green']]))
