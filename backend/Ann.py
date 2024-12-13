import torch
import numpy as np
import torch.nn as nn
import torch.nn.init as init

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class ANN_BlackScholes(nn.Module):
    def __init__(self, input_size, num_classes):
        super(ANN_BlackScholes, self).__init__()

        ''' Define layers '''
        self.fc1 = nn.Linear(input_size, 400)
        self.fc2 = nn.Linear(400, 400)
        self.fc3 = nn.Linear(400, 400)
        self.fc4 = nn.Linear(400, 400)
        self.fc5 = nn.Linear(400, num_classes)

        ''' Activation and dropout '''
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.0)

        ''' Apply Glorot (Xavier) initialization to the weights '''
        self._initialize_weights()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.relu(x)
        x = self.fc4(x)
        x = self.relu(x)
        x = self.fc5(x)
        return x

    def _initialize_weights(self):
        ''' Apply Glorot (Xavier) initialization to all layers '''
        init.xavier_uniform_(self.fc1.weight)
        init.xavier_uniform_(self.fc2.weight)
        init.xavier_uniform_(self.fc3.weight)
        init.xavier_uniform_(self.fc4.weight)
        init.xavier_uniform_(self.fc5.weight)