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
print("Build a tensor directly from data")
x = torch.tensor([5.5, 3])
print(x)

#Create a tensor based on a existing tensor
print("Create a Tensor based on a existing Tensor")
x = x.new_ones(5,3, dtype=torch.double)
print(x)

x = torch.rand_like(x, dtype=torch.float)
print(x)


#Getting tensor size - is a tuple
print(x.size())

#Tensor Operations
print("Tensors Operations - Addition")
y = torch.rand(5,3)
print(y)
print(x+y)

#Tensor Addition syntax 2
print("Addition Syntax 2")
print(torch.add(x,y))



#Providig an output tensor as argument
print("Providing an output as an argument")
result = torch.empty(5,3)
torch.add(x,y, out=result)
print(result)

#Addition: in place
print("Addition: in-place")
y.add_(x)
print(y)
print("Any opeartion that enumerate a tesnor in-place will change the tensor")

#Standard numpy notation
print("Standard numpy notation")
print(x)
print("All rows, second column")
print(x[:,1])


#Resizing tensors
print("Resizing tensors..")
x = torch.rand(4,4)
print(x)
y = x.view(16)
print(y)
z = x.view(-1,8) #Calculate just have 8 columns or 8 rows
print(z)
xx = x.view(8,-1)
print(x.size(),y.size(),z.size(), xx.size())

#Getting python number
print("Getting python number")
x = torch.randn(1)
print(x.item())




