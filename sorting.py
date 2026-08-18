
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88, 75, 95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Marks'])
plt.title('Student Marks')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



