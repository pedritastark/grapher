
import matplotlib.pyplot as plt



def lineal(m,x,b):
    return m*x + b

def cuadratic(a,x,b,c):
    return (a*x**2)+(b*x)+c


def plot_lineal():
    x = range (-10,10)
    m = 1
    b = 0
    plt.plot(x, [lineal(m,i,b) for i in x])
    rx = int(input("Rango"))
    ry = int(input("Dominio"))
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlim(-rx, rx)
    plt.ylim(-ry, ry)
    plt.savefig("output.png")
    plt.show()

def plot_cuadratic():
    x = range (-10,10)
    a = 2
    b = 3
    c = 0
    plt.plot(x, [cuadratic(a,i,b,c) for i in x])
    rx = int(input("Rango"))
    ry = int(input("Dominio"))
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlim(-rx, rx)
    plt.ylim(-ry, ry)
    plt.savefig("output.png")
    plt.show()