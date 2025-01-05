


import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('titanic.csv')

print(data.columns)
print(data.head)



"""
Assignment: Data Visualization Using a Health Dataset
Requirements
	•	Download dataset from github link :
	•	Use all visualization graph
	•	Line chart
	•	Bar plot
	•	Pie chart
	•	Box plot
	•	Histogram
	•	Scatter Plot
Also explain each findings from the graphUpload your github link
"""

# Line Chart
line_data = data.groupby('Pclass')['Survived'].sum()
plt.figure()
plt.plot(line_data.index, line_data.values)
plt.title('Survival by Passenger Class')
plt.xlabel('Pclass')
plt.ylabel('Survived')
plt.show()

# Bar Plot
bar_data = data['Embarked'].value_counts()
plt.figure()
plt.bar(bar_data.index, bar_data.values)
plt.title('Embarked Distribution')
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.show()

# Pie Chart
pie_data = data['Sex'].value_counts()
plt.figure()
plt.pie(pie_data.values, labels=pie_data.index, autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.show()

# Box Plot
plt.figure()
plt.boxplot(data['Age'].dropna())
plt.title('Age Distribution')
plt.ylabel('Age')
plt.show()

# Histogram
plt.figure()
plt.hist(data['Fare'], bins=20)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(data['Age'], data['Fare'], alpha=0.5)
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()