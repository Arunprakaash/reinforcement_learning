## snake_ai

This project uses Pygame and Reinforcement Learning with PyTorch to implement the classic Snake game. The goal is to train an agent to play the game autonomously and achieve the highest score possible.

### Requirements

* pygame==2.5.2
* torch==2.2.2
* torchvision==0.17.2
* matplotlib==3.8.4
* ipython==8.23.0

You can install the requirements by running:

```
pip install -r requirements.txt
```

### Training the Agent

To train the agent, run the `train.py` script:

```
python train.py
```

This will start the training process, and you can see the agent playing the game and improving over time. The current score and the record score will be printed in the console. The model weights will be saved every time a new record is achieved.

### Playing with the Trained Model

To play the game using the trained model, run the `play_game_with_model.py` script:

```
python play_game_with_model.py
```

This will load the saved model weights and start the game. The agent will play the game autonomously, and the final score will be printed in the console.

### Project Structure

* `agent.py`: contains the implementation of the Agent class, which includes the Q-learning algorithm and the neural network model.
* `snake_game.py`: contains the implementation of the Snake game using Pygame.
* `model.py`: contains the implementation of the neural network model and the QTrainer class.
* `train.py`: script to train the agent.
* `play_game_with_model.py`: script to play the game using the trained model.
* `requirements.txt`: list of required packages.
