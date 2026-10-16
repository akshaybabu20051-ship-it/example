from sklearn.model_selection import train_test_split
import pandas as pd
data = {
    "student_name": ["John", "Alice", "Bob", "Eve", "Charlie"],
    "student_age": [25, 30, 22, 28, 35],
    "student_course": ["Math", "Science", "History", "Art", "Music"],
    "student_nationality": ["USA", "USA", "USA", "USA", "USA"],  
    "department": ["Science", "Arts", "History", "Arts", "Music"]

}

data = pd.DataFrame(data)
data_train, data_test = train_test_split(data, test_size=0.2, random_state=42)

print("Training Data:")
print(data_train)
print("\nTesting Data:")
print(data_test)

student_name = data["student_name"]
print("Name of the columns in the DataFrame:", data.columns.tolist())
print("Number of rows and columns in the DataFrame:", data.shape)
