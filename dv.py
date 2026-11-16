import matplotlib.pyplot as graph
graph.plot([1,2,3,4,5],[1,2,3,4,5])


graph.title('graph')
graph.xlabel('x-axis')
graph.ylabel('y-axis')





graph.show()



'''comparison between the movies earning of YRF and T-seris '''

import matplotlib.pyplot as plt
a=[2002,2003,2004,2005,2006]
b=[244,674,45,456,565]
plt.plot(a,b,label='earning of movies by YRF')


plt.title('graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')



plt.legend()




x=[2002,2003,2004,2005,2006]
y=[212,100,30,542,230]

plt.plot(x,y,label='movies by t-seris earning')
plt.title('GRAPH OF REPRESENTING THE EARNING OF THE MOVIES SINCE 2002-2006')
plt.xlabel('years')
plt.ylabel('earning')
plt.legend()



plt.show ()