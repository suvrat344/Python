# Consider an intelligent traffic signal. The signal has two states: red and green. The vehicle density in front of the signal is denoted by the variable v. If the vehicle density crosses a threshold T in either direction, the state of the signal changes. The dynamics of this change is represented in the image given below:
# For example, if the signal is currently red, and the vehicle density becomes greater than or equal to the threshold, it is time to turn the signal green. This is denoted by the arrow from red to green at the bottom of the image. Assume that the signal senses the vehicle density every 30 seconds and updates its state appropriately.
# Write a class named Signal with the following specification:
# Attributes
# (1) state: string, either "red" or "green"; represents the current state of the signal
# (2) v: int, represents the vehicle density at the current instant
# (3) T: int, threshold for the vehicle density
# Methods
# self is the first argument of all methods. We will only mention additional arguments, if any.
# (1) __init__: constructor; accepts the threshold T as argument; initially the signal is red and the vehicle density is 0.
# (2) sense: accept the vehicle density as argument and update the corresponding attribute; assume that this information 
# comes from a sensor.
# (3) update: update the state of the signal-attribute depending on the current values of the attributes.
# (1) Each test case corresponds to one or more method calls. We will use S to denote the name of the object.
# Input                                   Expected Output
# Test Case1
# Signal(20)                                  red
# S.sense(15)
# S.update()
# print(S.state)
# Test Case2
# Signal(25)                                  red
# S.sense(20)                                 green
# S.update()                                  green
# print(S.state)
# S.sense(30)
# S.update()
# print(S.state)
# S.sense(40)
# S.update()
# print(S.state)                                           

class Signal:
    def __init__(self, T):
        self.state = 'red'
        self.v = 0
        self.T = T

    def sense(self, v):
        self.v = v

    def update(self):
        if self.v >= self.T:
            if self.state == 'red':
                self.state = 'green'
        else:
            if self.state == 'green':
                self.state = 'red'


signal = Signal(25)
signal.sense(20)                               
signal.update()                                 
print(signal.state)
signal.sense(30)
signal.update()
print(signal.state)
signal.sense(40)
signal.update()
print(signal.state) 