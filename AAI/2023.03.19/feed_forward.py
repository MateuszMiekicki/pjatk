import torch

w1 = torch.randn(784, 100, requires_grad=True)
b1 = torch.randn(1, 100, requires_grad=True)

w2 = torch.randn(100, 10, requires_grad=True)
b2 = torch.randn(1, 10, requires_grad=True)


def feed_forward(x):
    x = torch.relu(torch.mm(x, w1) + b1)
    x = torch.mm(x, w2) + b2
    return x


input_data = torch.randn(64, 784)
output = feed_forward(input_data)
print(output.shape)
