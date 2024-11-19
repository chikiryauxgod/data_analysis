import torch 
import numpy as np
print(torch.__version__)

data = np.array([[1, 2, 3], [4, 5, 6]])
#print(data)

t1 = torch.from_numpy(data) #torch.from_numpy()
print(t1)

t2 = torch.tensor(data) #torch.tensor()
#print(t2)

data[0, 0] = 100
print(t1)
print(data)