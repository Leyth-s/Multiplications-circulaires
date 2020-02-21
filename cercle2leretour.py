import matplotlib.pyplot as plt
from numpy import linspace, pi, cos, sin
import matplotlib.animation as animation
#from matplotlib import style


def table2(n, mod):
    """Trace la table de mutliplication "modulaire" de n modulo mod"""
    #tracé du cercle
    X1 = linspace(0, 2*pi, 1000)
    X = cos(X1)
    Y = sin(X1)
    plt.plot(X, Y, c='black', linewidth=0.5)
    #tracé des points
    pas = 2*pi / mod
    angle = pi/2
    x = []
    y = []
    for _ in range(mod): #à creuser
        x.append(cos(angle))
        y.append(sin(angle))
        angle -= pas
    plt.scatter(x, y, c='black', s = 1)
    #tracé de la table de multiplication modulaire
    for i in range(mod+1):
        q = n*i % mod
        x1 = [cos(pi/2 - q*2*pi/mod), x[i%mod]]
        y1 = [sin(pi/2 - q*2*pi/mod), y[i%mod]]
        plt.plot(x1, y1, c='black', linewidth=0.5)
    plt.axis('equal')
    plt.title('Table de {} modulo {}'.format(round(n, 2), mod))
    plt.show()

i = 360
while i < 500:
    table2(i, 300)
    plt.pause(0.01)
    plt.cla()
    i += 0.1
plt.show()
