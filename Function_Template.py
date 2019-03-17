import numpy as np
import matplotlib.pyplot as plt

#gives the set of x values that will be evaluated by f(x)
t = np.linspace(0, 1, 256, endpoint = True)

#f(x) equation
#-- equation goes here --

#plots f(x)
plt.plot(f, x)

#initializes the axes for the plot
axes = plt.gca()

#describes the horizontal and vertical ranges for the plot
axes.set_xlim([x.min(), x.max()])
axes.set_ylim([f.min(), f.max()])

#Places horizontal and vertical labels for the plot
plt.xlabel('x')
plt.ylabel('f')
#Places the title for the plot
plt.title('$f(x)')

#Puts a grid in the plot
plt.rc('grid', linestyle="-", color='black')
plt.grid(True)


plt.show()