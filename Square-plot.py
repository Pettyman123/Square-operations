import matplotlib.pyplot as plt
plt.axes()
rectangle = plt.Rectangle((0,0), 20, 20, fc='#EC79E0',ec="black")
plt.gca().add_patch(rectangle)
plt.axis('scaled')
plt.show()