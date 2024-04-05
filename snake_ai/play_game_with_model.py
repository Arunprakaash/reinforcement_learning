from agent import Agent
from snake_game import SnakeGameAI

game = SnakeGameAI()

# Initialize agent and load model weights
agent = Agent()
agent.load_model_weights('model/weights.pth')

# Game loop
while True:
    # Get state and action
    state_old = agent.get_state(game)
    final_move = agent.get_action(state_old)

    # Perform move and get new state
    reward, game_over, score = game.play_step(final_move)

    # If game over, break the loop
    if game_over:
        break

print('Final Score', score)
