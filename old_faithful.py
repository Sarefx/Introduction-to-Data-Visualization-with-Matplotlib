from itertools import groupby

import csv
import matplotlib.pyplot as plt

input_file = 'old_faithful.csv'

plt.figure(figsize=(7.5,4.25))
plt.style.use('classic')

with open(input_file, 'r') as old_faithful_data:
    eruptions = list(csv.reader(old_faithful_data))

eruptions.pop(0)

eruption_times = []
waiting_times = []

for event in range(0, len(eruptions)-1):
    eruption_times.append(float(eruptions[event][0]))
    waiting_times.append(float(eruptions[event][1]))

plt.subplot(2,2,1)
plt.boxplot(eruption_times)
plt.title('Old Faitful Eruprtions')
plt.xticks([1], ['Eruptions'])
plt.xlabel('Length of Eruption (mins)')

plt.subplot(2,2,2)
num_bins=8
plt.hist(eruption_times, num_bins)
plt.title('Old Faithful Eruptions')
plt.xlabel('Length of Eruption (mins)')

plt.subplot(2,2,3)
plt.boxplot(waiting_times)
plt.title('Old Faithful Waiting')
plt.xticks([1], ['Waiting'])
plt.xlabel('Length of Waiting (mins)')

plt.subplot(2,2,4)
plt.scatter(eruption_times, waiting_times)
plt.title('Old Faithful Eruptions')
plt.xlabel('Length of Eruption (mins)')
plt.ylabel('Time Between Eruptions (mins)')

plt.tight_layout()  # gives padding between charts, so things are not too close to each other
plt.show()
