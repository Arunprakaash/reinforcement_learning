import random
from collections import deque

import numpy as np
import torch
import torch.nn as nn


def masked_softmax(vec, mask, dim=1, epsilon=1e-5):
    exps = torch.exp(vec)
    masked_exps = exps * mask.float()
    masked_sums = masked_exps.sum(dim, keepdim=True) + epsilon
    return masked_exps / masked_sums


class DDQN(nn.Module):

    def __init__(self, inp_dim, action_dim):
        super(DDQN, self).__init__()

        self.epsilon = 1
        self.feature = nn.Sequential(
            nn.Linear(inp_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
        )

        self.advantage = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim)
        )

        self.value = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x, mask):
        x = x / 8
        x = self.feature(x)
        advantage = masked_softmax(self.advantage(x), mask)
        value = masked_softmax(self.value(x), mask)
        return value + advantage - advantage.mean()

    def act(self, state, mask):
        bruh = random.random()
        if bruh > self.epsilon:
            state = torch.FloatTensor(state).unsqueeze(0)
            mask = torch.FloatTensor(mask).unsqueeze(0)
            q_value = self.forward(state, mask)
            action = q_value.max(1)[1].data[0].item()
        else:
            indices = np.nonzero(mask)[0]
            rand_no = random.randint(0, len(indices) - 1)
            action = indices[rand_no]
        return action


class Buffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, mask, reward, new_state, new_mask, terminal):
        self.buffer.append((state, action, mask, reward, new_state, new_mask, terminal))

    def sample(self, batch_size):
        states, actions, masks, rewards, new_states, new_mask, terminals = zip(*random.sample(self.buffer, batch_size))
        return states, actions, masks, rewards, new_states, new_mask, terminals
