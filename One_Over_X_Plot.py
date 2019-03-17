import numpy as np
import matplotlib.pyplot as plt
import numpy.ma as ma

#constant parameters
step = .01#difference between consecutive x values 
tick_step = 1;#difference between consecutive tick marks
min_x = -8
max_x = 8
min_y = -8
max_y = 8
#discontinuities
d1 = 0


#segments of the domain divided by the discontinuities.
x1 = np.arange(min_x,d1,step)
x2 = np.arange(d1,max_x+step,step)


#functions for different segments of the domain.
y1 = lambda x: 1/x
y2 = lambda x: 1/x


#variable used to mask the closest values near the discontinuity.
e = 1.5*step 

#Mask values +/- e around discontinuities
mx1 = ma.masked_inside(x1,d1-e,d1+e)
mx2 = ma.masked_inside(x2,d1-e,d1+e)

#bring together all separate segments of the domain 
x = ma.concatenate([mx1,mx2])

#piecewise function declaration
f = np.piecewise(x,[x>0,x<0],[y1,y2])

#Plotting Configuration

plt.plot(x,f)#Plot function
plt.axis([min_x,max_x,min_y,max_y])#Sets up dimensions of axes
plt.xticks(np.arange(min_x, max_x+1, tick_step))#set up for the tick marks on the x axis
plt.yticks(np.arange(min_y, max_y+1, tick_step))#set up for the tick marks on the y axis

plt.show()#display plot