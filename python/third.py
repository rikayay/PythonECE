import matplotlib.pyplot as plt
import numpy as np
class subplot:
    def Plot():
        x_axis_1 = np.random.randint(10,22,12)
        y_axis_1 = np.random.randint(15,50,12)
        plt.subplot(3,3,1)
        plt.plot(x_axis_1, y_axis_1)

        x_axis_2 = np.random.randint(18,220,10)
        y_axis_2 = np.random.randint(16,25,10)
        plt.subplot(3,3,2)
        plt.plot(x_axis_2, y_axis_2)

        x_axis_3 = np.random.randint(10,22,14)
        y_axis_3 = np.random.randint(20,40,14)
        plt.subplot(3,3,3)
        plt.plot(x_axis_3, y_axis_3)

        x_axis_4 = np.random.randint(10,22,13)
        y_axis_4 = np.random.randint(14,65,13)
        plt.subplot(3,3,4)
        plt.plot(x_axis_4, y_axis_4)

        x_axis_5 = np.random.randint(19,21,12)
        y_axis_5 = np.random.randint(15,50,12)
        plt.subplot(3,3,5)
        plt.plot(x_axis_5, y_axis_5)

        x_axis_6 = np.random.randint(182,220,10)
        y_axis_6 = np.random.randint(160,215,10)
        plt.subplot(3,3,6)
        plt.plot(x_axis_6, y_axis_6)

        x_axis_7 = np.random.randint(10,22,14)
        y_axis_7 = np.random.randint(20,40,14)
        plt.subplot(3,3,7)
        plt.plot(x_axis_7, y_axis_7)

        x_axis_8 = np.random.randint(10,22,13)
        y_axis_8 = np.random.randint(14,65,13)
        plt.subplot(3,3,8)
        plt.plot(x_axis_8, y_axis_8)

        x_axis_9 = np.random.randint(10,22,13)
        y_axis_9 = np.random.randint(14,65,13)
        plt.subplot(3,3,9)
        plt.plot(x_axis_9, y_axis_9)

        plt.show()

subplot.Plot()