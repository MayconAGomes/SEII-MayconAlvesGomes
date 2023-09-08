import numpy as np

a = np.array([[1,2], [3,4]])

print(np.linalg.inv(a))
print(np.linalg.det(a))
print(np.diag(a))

c = np.diag(a)
print(np.diag(c))