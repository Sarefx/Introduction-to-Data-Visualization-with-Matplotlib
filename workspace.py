import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

plt.plot([1,2,3,4], [1,4,9,16], color='green', linestyle='dashdot')
plt.plot([2,3,4,5], [2,3,4,5], color='#2B5B84', linestyle='dashed')
plt.ylabel('Important Figures')  # adds a Y label to the chart
plt.legend()  # adds a legend to the chart
#plt.show()  # displays the chart



panel_1 = plt2.subplot(2,1,1)  # creates parameters for the panel
plt2.plot([1,2,3,4], [1,4,9,16], color='green', linestyle='dashdot')
panel_1.set_xlim([0,6])  # sets x limit to 6
panel_1.set_ylim([0,20])


panel_2 = plt2.subplot(2,1,2)
plt2.plot([2,3,4,5], [2,3,4,5], color='#2B5B84', linestyle='dashed')
panel_2.set_xlim([0,6])
panel_2.set_ylim([0,20])

plt2.show() 
