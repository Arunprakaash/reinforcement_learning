import time

import torch

from env import MineSweeper
from model import DDQN
from render_ui import Render


class Tester:
    def __init__(self, render_flag):
        self.model = DDQN(36, 36)
        self.render_flag = render_flag | True
        self.width = 6
        self.height = 6
        self.env = MineSweeper(self.width, self.height, 6)
        if self.render_flag:
            self.renderer = Render(self.env.state)
        self.load_models(20000)

    def get_action(self, state):
        state = state.flatten()
        mask = (1 - self.env.fog).flatten()
        action = self.model.act(state, mask)
        return action

    def load_models(self, number):
        path = "./weights/model" + str(number) + ".pth"
        model_dict = torch.load(path)
        self.model.load_state_dict(model_dict['current_state_dict'])
        self.model.epsilon = 0

    def do_step(self, action):
        i = int(action / self.width)
        j = action % self.width

        next_state, terminal, reward = self.env.choose(i, j)

        if self.render_flag:
            self.renderer.state = self.env.state
            self.renderer.draw(save_gif=True, is_terminal = terminal)
            self.renderer.bug_fix()

        return next_state, terminal, reward


def win_tester(games_no):
    tester = Tester(False)
    state = tester.env.state
    mask = tester.env.fog
    wins = 0
    i = 0
    step = 0
    first_loss = 0
    while i < games_no:
        step += 1
        action = tester.get_action(state)
        next_state, terminal, reward = tester.do_step(action)
        state = next_state
        if terminal:
            if step == 1 and reward == -1:
                first_loss += 1
            i += 1
            tester.env.reset()
            state = tester.env.state
            if reward == 1:
                wins += 1
            step = 0

    print("Win Rate: " + str(wins * 100 / games_no))
    print("Win Rate excluding First Loss: " + str(wins * 100 / (games_no - first_loss)))


def slow_tester():
    tester = Tester(True)
    state = tester.env.state
    count = 0
    start = time.perf_counter()
    step = 0
    first_loss = 0

    while True:
        count += 1
        step += 1
        action = tester.get_action(state)
        next_state, terminal, reward = tester.do_step(action)
        state = next_state
        print(reward)
        time.sleep(0.5)

        if terminal:
            if reward == 1:
                print("WIN")
            else:

                print("LOSS")
            tester.env.reset()
            step = 0
            state = tester.env.state
            break


def main():
    slow_tester()


main()
