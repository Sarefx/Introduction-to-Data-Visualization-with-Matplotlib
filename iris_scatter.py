from itertools import groupby

import csv
import matplotlib.pyplot as plt

input_file = 'iris.csv'

plt.figure(figsize=(7.5,4.25))

with open(input_file, 'r') as iris_data:  # open the file (r stands for read only) and saves it as iris_data
    irises = list(csv.reader(iris_data))  # reads csv structured data and transfers it to py list

colors = {"Iris-setosa": "#2B5B84", "Iris-versicolor": "g", "Iris-virginica": "purple"}

for species, group in groupby(irises, lambda i: i[4]):
    #print("species is",species)
    print("group is",group)
    categorized_irises = list(group)
    sepal_lengths = [float(iris[0]) for iris in categorized_irises]
    sepal_widths = [float(iris[1]) for iris in categorized_irises]
    plt.scatter(sepal_lengths, sepal_widths, s=10, c=colors[species], label=species)


plt.title("Fisher's Iris Data Set", fontsize=12)
plt.xlabel("sepal length (cm)", fontsize=10)
plt.ylabel("sepal width (cm)", fontsize=10)
plt.legend(loc="upper right")

plt.show()
