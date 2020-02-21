import matplotlib.pyplot as plt
from numpy import linspace, pi, cos, sin
from matplotlib import style

def table(n, p, mod, r=1):
    """Trace la table de mutliplication "modulaire" de n modulo mod sur un cercle de rayon r"""
    #tracé du cercle
    X1 = linspace(0, 2*pi, 1000)
    X = r*cos(X1)
    Y = r*sin(X1)
    plt.plot(X, Y, c='w')
    #tracé des points
    pas = 2*pi / mod
    angle = pi/2
    x = []
    y = []
    for _ in range(mod): #à creuser
        x.append(r*cos(angle))
        y.append(r*sin(angle))
        angle -= pas
    plt.scatter(x, y, c='w')
    #tracé de la table de multiplication modulaire
    for i in range(p+1):
        q = n*i % mod
        x1 = [x[q%mod], x[i%mod]]
        y1 = [y[q%mod], y[i%mod]]
        plt.plot(x1, y1, c='w')
    plt.axis('equal')
    plt.title('Table de {} modulo {}'.format(n, mod))
    plt.style.use('fast')
    plt.savefig('/home/leyth/Bureau/imagecercle2.png', dpi=100, bbox_inches='tight')
    plt.show()
for i in range(360, 500):
    table(i, 300, 300, 100)
    plt.pause(0.01)
    plt.cla()
plt.show()
