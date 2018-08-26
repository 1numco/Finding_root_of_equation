import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return 5**x+3*x             #you can enter your function
def graph():
    X=np.linspace(-1,1)
    Y=func(X)
    plt.plot(X,Y)
    plt.grid()
    plt.show()
def derivative(x):
    delta=0.000000000001
    return (func(x+delta)-func(x-delta))/(2*delta)
def null():

    x0=0          #approximate initial value of the function argument(it is adjustable using a graph)
    x1=x0-func(x0)/derivative(x0)     #new value of the function according to the method of Newton
    it=0
    e=0.0001
    while abs(x0-x1)>e and it<200:     #iterative process
        it+=1
        x0=x1
        if func(x1)!=0:
            x1=x0-func(x0)/derivative(x0)              
    print("Null of function: ",x1)
    print("Value of the function in the null: ", func(x1))
graph()
null()
n=input("Press Enter to exit.")