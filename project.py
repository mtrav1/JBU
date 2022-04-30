import matplotlib.pyplot as plt
import numpy as np
import time as t

smartvalue, strongvalue,breedvalue,normalvalue = np.loadtxt('sharedfile2.txt', delimiter=',', unpack=True)

typearray = ["Smart","Strong","Breed","Normal"]
numberarray = [smartvalue,strongvalue,breedvalue,normalvalue]

plt.title('Line Graph using NUMPY')
plt.xlabel('Normal monkeys')
plt.ylabel('Number of monkeys')
figure, ax = plt.subplots(figsize=(1,5))
plt.ion()
plot1, = ax.plot(typearray, numberarray,marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")

plt.show()
while True:
    smartvalue, strongvalue, breedvalue, normalvalue = np.loadtxt('sharedfile2.txt', delimiter=',', unpack=True)
    numberarray = [smartvalue, strongvalue, breedvalue, normalvalue]
    update_y_value = numberarray

    plot1.set_ydata(update_y_value)
    figure.tight_layout()
    figure.canvas.draw()
    figure.canvas.flush_events()
    t.sleep(0.1)




    
