# play_game_with_model.py

import numpy as np
import torch

from agent import Agent
from model import LinearQNet
from snake_game import SnakeGameAI

# Instantiate your LinearQNet model
input_size = 11
hidden_size = 256
output_size = 3
model = LinearQNet(input_size, hidden_size, output_size)

# Load the weights into the model
file_name = 'weights.pth'
model.load(file_name)

# Instantiate the game and agent
game = SnakeGameAI()
agent = Agent()

# Play the game using the loaded model weights
while True:
    state = agent.get_state(game)
    state_tensor = torch.tensor(state, dtype=torch.float).unsqueeze(0)
    prediction = model(state_tensor)
    action = np.argmax(prediction.detach().numpy())
    reward, game_over, score = game.play_step(action)
    if game_over:
        break

print('Final Score:', score)
