import csv
import matplotlib.pyplot as plt

input_file = 'iris.csv'

plt.figure(figsize=(7.5,4.25))
plt.style.use('classic')

with open(input_file, 'r') as iris_data:  # open the file (r stands for read only) and saves it as iris_data
    irises = list(csv.reader(iris_data))  # reads csv structured data and transfers it to py list

colors = {"Iris-setosa": "#2B5B84", "Iris-versicolor": "g", "Iris-virginica": "purple"}

virginica_petal_length = []

num_bins = 10

for petal in range(0, len(irises)-1):
    if irises[petal][4] == 'Iris-virginica':
        virginica_petal_length.append(float(irises[petal][2]))

plt.hist(virginica_petal_length, num_bins, facecolor='red', alpha=0.75)
plt.title('Iris-virginica Petale length', fontsize=12)
plt.xlabel('Petal length (cm)', fontsize=10)
plt.ylabel('Probability', fontsize=10)

plt.show()
