# handelling imbalanced dataset:
# up sampling, down sampling:
import numpy as np
import pandas as pd

# set the random seed for reproductiblity:
np.random.seed(123)

# create a dataset with two classes:
n_sample = 1000
class_0_ratio = 0.9
n_class_0 = int(n_sample*class_0_ratio)
n_class_1 = n_sample - n_class_0

print(n_class_0, n_class_1)

# create my dataframe with imbalanced dataset:
class_0 = pd.DataFrame({
    'feature1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0]*n_class_0
})

class_1 = pd.DataFrame({
    'feature1': np.random.normal(loc=2, scale=1, size=n_class_1),
    'feature2': np.random.normal(loc=2, scale=1, size=n_class_1),
    'target': [1]*n_class_1
})

pd.concat([class_0, class_1]).reset_index(drop=True)