# minesweeper_ai

This project implements a MineSweeper game environment and trains a Deep Q-Network (DQN) agent to play the game using PyTorch. The project consists of several Python files:

- `env.py`: Defines the MineSweeper environment.
- `minesweeper_agent.py`: Implements a testing module for the DDQN agent.
- `train.py`: Contains the training loop for the DDQN agent.
- `render_ui.py`: Provides a simple UI for visualizing the MineSweeper game.
- `model.py`: Defines the DQN neural network model and a buffer for experience replay.


### Usage

#### Training the Agent
To train the DQN agent, run:

```bash
python train.py
```

This will train the agent for a specified number of epochs, saving checkpoints every specified number of batches.

#### Testing the Agent
To test the trained DQN agent, run:

```bash
python minesweeper_agent.py
```
This will test the agent's performance over a specified number of games and print out the win rate.




