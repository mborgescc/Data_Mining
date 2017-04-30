import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def generate_linear_data(w,b,n):
    dim = len(w)
    y = []
    X = []
    for i in xrange(n):
        x = np.random.uniform(-10,10,dim)
        if(np.dot(w,x) + b > 5):
            y.append(1)
            X.append(x)
        elif(np.dot(w,x) + b < -5):
            y.append(-1)
            X.append(x)
    return np.array(X),y

def sign(v):
	if v < 0:
		return -1
	else:
		return 1

w = np.random.uniform(-3,3,3)
b = 3
X, y = generate_linear_data([-1, 2, 3],b,10)

print "w: %s" % w
print "X: %s" % X
print "y: %s" % y
print " "

for i in xrange(0,len(X)):
	if not sign(np.dot(w,X[i]) + b) == sign(y[i]):
		# w = w + y[i]*x[i]
		w = np.add(w, np.multiply(y[i], X[i]))

print "Terminado"
print "w: %s" % w

'''
def plot_points(X,y):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X1 = []
    X2 = []
    for i in xrange(len(y)):
        if (y[i] == -1):
            X1.append(X[i])
        else:
            X2.append(X[i])
    X1 = np.array(X1)
    X2 = np.array(X2)
    ax.scatter(X1[:,0], X1[:,1], X1[:,2], c='blue', marker='^')
    ax.scatter(X2[:,0], X2[:,1], X2[:,2], c='red', marker='o')

plot_points(X, y)
plt.show()
'''