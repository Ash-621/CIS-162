import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen (green)', 'sophomores (blue)', 'juniors (pink)', 'seniors (yellow)']
colorlist = ['green', 'blue', 'pink', 'yellow' ]
explodelist = [0.05, 0.025, 0.013, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 35)
plot.axis('equal')
plot.savefig('piechart.png')

