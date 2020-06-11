import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    def __init__(self, state_size, action_size, seed, h1_units=128, h2_units=128):
        """Initialize parameters and build model
        
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimesion of each action
            seed (int): Random seed
            h1_units (int): Number of nodes in the first hidden layer
            h2_units (int): Number of nodes in the second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.h1 = nn.Linear(state_size, h1_units)
        self.h2 = nn.Linear(h1_units, h2_units)
        self.h3 = nn.Linear(h2_units, action_size)
        
    def forward(self, state):
        x = F.relu(self.h1(state))
        x = F.relu(self.h2(x))
        return self.h3(x)
        
    