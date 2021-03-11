import numpy as np

'''
Perceptron:
Binary Classifier
Artificial neuron
Multiple input=>One Output (Binary)


'''

def And(x1,x2):
    w1=0.5
    w2=0.5
    theta=0.5
    res=w1*x1+w2*x2
    if res>theta:
        return 1
    else:
        return 0

def OR(x1,x2):
    w1=0.5
    w2=0.5
    theta=0.4
    res=w1*x1+w2*x2
    if res>theta:
        return 1
    else:
        return 0


def NAND(x1,x2):
    w1=0.5
    w2=0.5
    theta=0.5
    res=w1*x1+w2*x2
    if res>theta:
        return 0
    else:
        return 1
    

print("===AND===")
print("1,0=",And(1,0))
print("0,1=",And(0,1))
print("0,0=",And(0,0))
print("1,1=",And(1,1))

print("===OR===")
print("1,0=",OR(1,0))
print("0,1=",OR(0,1))
print("0,0=",OR(0,0))
print("1,1=",OR(1,1))

print("===NAND===")
print("1,0=",NAND(1,0))
print("0,1=",NAND(0,1))
print("0,0=",NAND(0,0))
print("1,1=",NAND(1,1))

def AndWithBias(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.5
    res=np.sum(w*x)+b
    if res<=0:
        return 0
    else:
        return 1
def ORWithBias(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.4
    res=np.sum(w*x)+b
    if res<=0:
        return 0
    else:
        return 1

def NANDWithBias(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.5
    res=np.sum(w*x)+b
    if res<=0:
        return 1
    else:
        return 0

print("===AND with Bias===")
print("1,0=",AndWithBias(1,0))
print("0,1=",AndWithBias(0,1))
print("0,0=",AndWithBias(0,0))
print("1,1=",AndWithBias(1,1))

#XOR Gate=> Can't make with a perceptron (it need perceptrons(multi-layer perceptron))
#XOR
#1,1=0
#1,0=1
#0,1=1
#0,0=0

def XOR(x1,x2):
    s1=NANDWithBias(x1,x2)
    s2=OR(x1,x2)
    res=AndWithBias(s1,s2)
    return res

print("===XOR===")
print("1,0=",XOR(1,0))
print("0,1=",XOR(0,1))
print("0,0=",XOR(0,0))
print("1,1=",XOR(1,1))
