# -*- coding: utf-8 -*-
"""LinearRegression-model2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n0S2hqfDyuXvZG1Tnt6frADq_w9XsvLu
"""

import numpy as np

theta0=0
theta1=0.5

#cost function

def cost_function(x,y,theta0,theta1):
  m=len(y)
  y_pred=theta0+theta1*x
  J_theta=(1/(2*m)) * np.sum((y_pred-y)**2)
  return J_theta

def gradient_descent(x,y,theta0,theta1,alpha,num_iterations):
  m=len(y)
  J_history= np.zeros(num_iterations)
  for i in range(num_iterations):
    y_pred= theta0+theta1*x
    dtheta0=(1/m) * np.sum(y_pred-y)
    dtheta1=(1/m) * np.sum((y_pred-y) * x)
    theta0=theta0 - alpha * dtheta0
    theta1=theta1- alpha * dtheta1
  return theta0, theta1, J_history

x= np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
y= np.array([245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000])

alpha=0.0000001
num_iterations=10000
theta0, theta1, J_history= gradient_descent(x,y,theta0,theta1,alpha,num_iterations)

print("theta_0:",theta0)
print("theta_1:",theta1)

#to plot the cost function
import matplotlib.pyplot as plt

plt.plot(J_history)
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.show()

# data and regression line

plt.scatter(x,y)
plt.plot(x,theta0+theta1*x,color='green')
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()