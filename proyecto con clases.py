import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
# import Tkinter as tk
class Graph:

    def grapher(action):
       
        def wrapper(*args):
            print(args)
            X = np.arange(-55,55)
            Y = [action(*args, x) for x in X]
            plt.plot(X, [action(*args,x) for x in X],'g' )
            plt.axhline(0, color='black',linestyle = '-')
            plt.axvline(0, color='black',linestyle = '-')
            plt.gca().spines['right'].set_visible(False)
            plt.gca().spines['top'].set_visible(False)
            plt.gca().spines['bottom'].set_visible(False)
            plt.gca().spines['left'].set_visible(False)
            plt.title(r'$Graph $')
            plt.grid('on', linestyle = '--')
            plt.show()
                ### tab
            D = [(xv, Y[xi]) for xi,xv in enumerate(X)]
           
                ### Tab 10-10
            D2 = [ d2x for d2i,d2x in enumerate(D) if d2i%10 == 0]
            print(tabulate(D2, headers = ["X", "Y"],tablefmt="fancy_grid"))
           
               
                ### Tab 4-4 / 1
#            for xi in range(0,len(D), 4):
#                T = [ D[ti] for ti in range(xi-4, xi+1)]
#                print(tabulate(T, headers = ["X", "Y"],tablefmt="fancy_grid"))
#                input()
     
        return wrapper
   


    @grapher
    def lineal(self, m,b,x):
        return m*x + b
   
    
Graph().lineal(5, 100)
    
    

   
   