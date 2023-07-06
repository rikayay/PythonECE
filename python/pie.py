import matplotlib.pyplot as plt
import numpy as np

y = np.array([20, 40, 5, 10])
mylabels = ["tulip", "sunflower", "rose", "hibiscus"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Flowers:")
plt.show() 