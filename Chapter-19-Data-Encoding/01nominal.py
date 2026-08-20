import pandas as pd
from sklearn.preprocessing import OneHotEncoder
# create a simple dataframe:
df = pd.DataFrame({
    'color':['red', 'blue', 'green', 'green', 'red', 'blue']
})
print(df.head())

# create an instance of one hot encoder
encoder = OneHotEncoder()
# perform fit and transform
encoded = encoder.fit_transform(df[['color']]).toarray()
encoder_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())
print(encoder_df)

'''
^^
||
||
||
this way we transform categorical data into numerical data
'''
# for new data:
print(encoder.transform([['blue']]).toarray())
print(pd.concat([df, encoder_df], axis=1))