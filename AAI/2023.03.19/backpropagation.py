import torch

input_size = 784
hidden_size = 100
output_size = 10

learning_rate = 5e-6
num_epochs = 600
batch_size = 64

x = torch.randn(input_size, batch_size)
y = torch.randn(output_size, batch_size)

w1 = torch.randn(hidden_size, input_size, requires_grad=True)
b1 = torch.randn(hidden_size, 1, requires_grad=True)
w2 = torch.randn(output_size, hidden_size, requires_grad=True)
b2 = torch.randn(output_size, 1, requires_grad=True)

for epoch in range(num_epochs):
    z1 = torch.mm(w1, x) + b1
    a1 = torch.relu(z1)
    z2 = torch.mm(w2, a1) + b2
    a2 = torch.relu(z2)

    loss = torch.mean(torch.square(y - a2))

    loss.backward()

    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        b1 -= learning_rate * b1.grad
        w2 -= learning_rate * w2.grad
        b2 -= learning_rate * b2.grad

        w1.grad.zero_()
        b1.grad.zero_()
        w2.grad.zero_()
        b2.grad.zero_()

    if (epoch+1) % 50 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
