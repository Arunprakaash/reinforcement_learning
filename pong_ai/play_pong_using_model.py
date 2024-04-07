from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_atari_env

env = make_atari_env("PongNoFrameskip-v4", n_envs=1, seed=0)
model = A2C.load("model/weights", verbose=1)

episodes = 1
for _ in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        env.render(mode="human")
        action, _states = model.predict(obs)
        observation, rewards, done, info = env.step(action)

env.close()
