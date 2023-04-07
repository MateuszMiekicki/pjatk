import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# define neural network


class Model(nn.Module):
    def __init__(self, input_size, num_classes):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(input_size, 200)
        self.fc2 = nn.Linear(200, 100)
        self.fc3 = nn.Linear(100, num_classes)

    def forward(self, x):
        out = F.relu(self.fc1(x))
        out = F.relu(self.fc2(out))
        out = self.fc3(out)
        if not self.training:
            out = F.softmax(out, dim=1)
        return out


# set up data
batch_size = 64
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_dataset = datasets.MNIST(
    root='./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=batch_size, shuffle=True)
test_dataset = datasets.MNIST(
    root='./data', train=False, download=True, transform=transform)
test_loader = torch.utils.data.DataLoader(
    test_dataset, batch_size=batch_size, shuffle=True)

# initialize model, loss function, and optimizer
input_size = 784
num_classes = 10
learning_rate = 0.001
model = Model(input_size, num_classes)
loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# train the model
train_losses = []
test_losses = []
for epoch in range(10):
    epoch_train_loss = 0.
    epoch_test_loss = 0.
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data.view(-1, input_size))
        loss = loss_function(output, target)
        loss.backward()
        optimizer.step()
        epoch_train_loss += loss.item()
    train_losses.append(epoch_train_loss/len(train_loader))

    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(test_loader):
            output = model(data.view(-1, input_size))
            loss = loss_function(output, target)
            epoch_test_loss += loss.item()
        test_losses.append(epoch_test_loss/len(test_loader))

    print(f"Epoch {epoch} train loss {epoch_train_loss/len(train_loader)}, test_loss {epoch_test_loss/len(train_loader)}")

# plot losses
plt.plot(list(range(10)), train_losses)
plt.plot(list(range(10)), test_losses)
plt.show()
