'''
- Neural Network
Input Layer/Hidden Layer/Output Layer

y=h(b+w1*x1+w2*x2)
=>h(X) => 0 or X

h(X): Activation Function

a=b+w1*x1+w2*x2
y=h(a)

'''


import numpy as np
import matplotlib.pylab as plt
#Make Activation Function



#step Fuction
def StepFuctionForBuiltinType(x):
    if x>0:
        return 1
    else:
        return 0

def StepFuctionForNumpyArray(x):
    y=x>0
    return y.astype(np.int)

x=np.array([-1.0,1.0,4.0,-0.5])

#[0 1 1 0]
print(StepFuctionForNumpyArray(x))

#Show Graph using matplotlib(Step Fuction)
x=np.arange(-5.0,5.0,0.1)
y=StepFuctionForNumpyArray(x)
plt.plot(x,y)
plt.ylim(-0.1,1,1)
plt.show()


#sigmoid function : h(x)=1/1+exp(-x)

def sigmoid(x):
    return 1/(1+np.exp(-x))

#Draw Graph using matplotlib(Sigmoid Fuction)

y=sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

#ReLU Function : 
#if input value is over 0, output is equal to input value. but input value is below 0, output is 0
# REctified Linear Unit Function  
def relu(x):
    return np.maximum(0,x)

y=relu(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()