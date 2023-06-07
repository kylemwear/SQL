import csv
import matplotlib.pyplot as plt

# Create an empty dictionary to store name-weight pairs
data = {}

# Read name and weight data from CSV file
with open('Crash Airlines 1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        weight = float(row[1])
        data[name] = weight

# Extract names and weights from the dictionary
names = list(data.keys())
weights = list(data.values())

# Create the bar chart
plt.barh(names, weights)

# Add labels and title
plt.xlabel('Bag Weight in Pounds')
plt.ylabel('Passengers')
plt.title('Passengers with Checked Bags Weighing Greater than 10Lbs.')

# Display the chart
plt.show()







