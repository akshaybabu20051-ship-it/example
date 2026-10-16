import pandas as pd 
from sklearn.model_selection import train_test_split
data = {
    "name": ["John", "Alice", "Bob", "Eve", "Charlie"],
    "age": [25, 30, 22, 28, 35],
    "country": ["USA", "USA", "USA", "USA", "USA"],
    "course": ["Math", "Science", "History", "Art", "Music"]
    
}

data = pd.DataFrame(data)
data_train, data_test = train_test_split(data, test_size=0.2, random_state=42)

print("Training Data:")
print(data_train)
print("\nTesting Data:")
print(data_test)


print("name of the columns in the DataFrame:", data.columns.tolist())
print("number of rows and columns in the DataFrame:", data.shape)
print("data types of each column in the DataFrame:", data.dtypes)   


a =30
b=20
sum = a + b
print("The sum of {} and {} is {}".format(a, b, sum))
