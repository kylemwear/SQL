import csv
import matplotlib.pyplot as plt

# Labels for pie chart
labels = 'Brazil', 'United States', 'Mexico', 'France'

# Give the path to the CSV file
path = 'Crash Airlines 2.csv'
amounts = []
# Open the file with path from above
with open(path, 'r') as file:
    # Create a CSV reader 
    reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        
        #get amount of current row and append to amounts list
        amount = int(row[0])
        amounts.append(amount)
            

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(amounts, labels = labels, autopct = '%1.1f%%',
       colors = ['darkcyan', 'firebrick', 'limegreen', 'royalblue'])
plt.title('Number of Passengers Flying From Each Country') 
# Display the bar chart
plt.show()








