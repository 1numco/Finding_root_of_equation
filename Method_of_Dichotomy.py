import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return 5**x+3*x             #you can enter your function
def graph(x0,x1):
    X=np.linspace(x0, x1)          
    Y=func(X)
    plt.plot(X,Y)
    plt.grid()
    plt.show()
def null(x0,x1):  
    it=0
    e=0.0001
    x2=(x1+x0)/2
    while abs(x0-x1)>e and it<200:    
        it+=1
        if func(x1)*func(x2)<0:
            x0=x2
        else:
            x1=x2
        x2=(x1+x0)/2
    print("Null of function: ",x1)
    print("Value of the function in the null: ", func(x1))
x0=-1
x1=1       #select the segment where zero is supposed to be
graph(x0,x1)
null(x0,x1)
n=input("Press Enter to exit.")