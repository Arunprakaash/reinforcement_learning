import argparse

from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_atari_env


def train(rl_model, total_timesteps):
    rl_model.learn(total_timesteps=total_timesteps)
    rl_model.save(f"model/weights")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train A2C model for Atari environment")
    parser.add_argument("--load", action="store_true", help="Load pre-trained weights")
    parser.add_argument("--continue_training", action="store_true", help="Continue learning after loading weights")
    parser.add_argument("--total_timesteps", type=int, default=100000, help="Total timesteps for training")
    args = parser.parse_args()

    env = make_atari_env("PongNoFrameskip-v4", n_envs=1, seed=0)

    if args.load:
        model = A2C.load("model/weights", verbose=1)
        model.set_env(env)
        if args.continue_training:
            train(model, args.total_timesteps)
    else:
        model = A2C("CnnPolicy", env, verbose=1)
        train(model, args.total_timesteps)
