# using metaplotlib to make data as bars

from matplotlib import pyplot as ppl

x=[2,5,4,2.2,8,9] #data for x axis
y=[1,6,5,3,6,2] #data for y axis
ppl.title("testing data")  #title of bar
ppl.bar(x,y)  #plot graph as bar
ppl.show() # to show the graph

# ppl.bar(x,y)
# ppl.show