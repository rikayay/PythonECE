import matplotlib.pyplot  as plt
import numpy as np
class Graph():
        x_axis_1 = np.random.randint(10,22,12)
        y_axis_1 = np.random.randint(15,50,12)
        plt.subplot(2,2,1)
        plt.plot(x_axis_1, y_axis_1)

        x_axis_2 = np.random.randint(18,220,10)
        y_axis_2 = np.random.randint(16,25,10)
        plt.subplot(2,2,2)
        plt.plot(x_axis_2, y_axis_2)

        x_axis_3 = np.random.randint(10,22,14)
        y_axis_3 = np.random.randint(20,40,14)
        plt.subplot(2,2,3)
        plt.plot(x_axis_3, y_axis_3)

        x_axis_4 = np.random.randint(10,22,13)
        y_axis_4 = np.random.randint(14,65,13)
        plt.subplot(2,2,4)
        plt.plot(x_axis_4, y_axis_4)

        plt.show()

subplot.Plot()