# create a simple dataframe with a categorical variable and a target varible:
import pandas as pd
df = pd.DataFrame({
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'New York', 'Paris'],
    'price': [200, 150, 300, 250, 180, 320]
})
print(df.head())

mean_price = df.groupby('city')['price'].mean().to_dict()
print(mean_price)
df['city_encoded'] = df['city'],map(mean_price)