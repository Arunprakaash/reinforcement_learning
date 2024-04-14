from model import BlackjackQLearning


def main():
    # Train the agent
    agent = BlackjackQLearning(load_pretrained_model=True)

    print("-----")
    result = agent.play()
    print(result)

    test_games = 1000000
    wins = 0
    losses = 0
    draws = 0

    for _ in range(test_games):
        print("-----")
        result = agent.play()
        print(result)
        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            draws += 1

    print(f"Wins: {wins}, Losses: {losses}, Draws: {draws}")
    print(f"Win rate: {wins / (wins + losses) * 100:.2f}%")


if __name__ == "__main__":
    main()
