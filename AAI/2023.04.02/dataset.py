from torch.utils.data import DataLoader
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset


mnist = fetch_openml("mnist_784")
data = mnist.data.to_numpy() / 255.0  # Normalize pixel values to 0-1 range
targets = np.vectorize(lambda x: int(x))(mnist.target.to_numpy())

train_data, test_data, train_targets, test_targets = train_test_split(
    data, targets, test_size=0.2, stratify=targets)


class DigitsDataset(Dataset):
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, idx):
        x = torch.tensor(self.data[idx], dtype=torch.float32)
        y = torch.tensor(self.targets[idx], dtype=torch.long)
        return x, y


train_dataset = DigitsDataset(train_data, train_targets)
test_dataset = DigitsDataset(test_data, test_targets)

batch_size = 128

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size)
