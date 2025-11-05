#4.2 1)
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 3, 1, 1, 2, 1, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'yes',
                'yes', 'no', 'no', 'no', 'yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']

# Create DataFrame
df = pd.DataFrame(exam_data, index=labels)
print("DataFrame:")
print(df)


#4.2 2)

df.loc[df['name'] == 'James', 'name'] = 'Suresh'
print("After changing 'James' to 'Suresh':")
print(df)


#4.2 3
df['age'] = [21, 23, 20, 25, 22, 24, 23, 21, 20, 26]
print("DataFrame after inserting new column 'age':")
print(df)

#4.2 4)
columns_list = df.columns.tolist()
print("List of DataFrame column headers:")
print(columns_list)

#4.2 5)
index_list = df.index.tolist()
print("List of DataFrame index labels:")
print(index_list)