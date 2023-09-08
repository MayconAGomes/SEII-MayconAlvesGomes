import numpy as np

# np.loadtxt, np.genfromtxt

data = np.loadtxt("spambase.csv", delimiter = ",", dtype=np.float32)
print(data.shape)

data = np.genfromtxt("spambase.csv", delimiter = ",", dtype=np.float32)
print(data.shape)