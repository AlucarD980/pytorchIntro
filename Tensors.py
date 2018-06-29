from __future__ import print_function
import torch

#Build an empty matrix
print("Empty matrix")
x = torch.empty(5,3)
print(x)


#Build a random matrix
print("Random Matrix")
x = torch.rand(5,3)
print(x)


#Build zeroa matrix
print("Zeros Matrix and dtype long")
x = torch.zeros(5, 3, dtype=torch.long)
print(x)


#build a tensor directly from data
x = torch.tensor([5.5, 3])
print(x)