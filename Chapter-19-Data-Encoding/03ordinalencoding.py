import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# create a simple dataframe:
df = pd.DataFrame({
    'size':['small', 'medium', 'large', 'medium', 'small', 'large']
})
print(df.head())


# create an instance for ordinal encoder and then perform fit_transform:
encoder = OrdinalEncoder(categories=[["small","medium","large"]])
encoded = encoder.fit_transform(df[['size']])
print(encoded)

# for ranks the above program