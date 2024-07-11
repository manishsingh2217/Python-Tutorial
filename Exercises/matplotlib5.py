# using metaplotlib to make data as pie chart
from matplotlib import pyplot as ppl

# data of pie chart
labels=['manish','saurabh','satyam']
size=[40,30,30] 

# plotting the pie chart
ppl.pie(size,labels=labels,autopct='%1.1f%%',startangle=90)
ppl.show()