## Atari A2C Training with Stable Baselines3

This project provides a Python script for training an A2C (Advantage Actor-Critic) model using the Stable Baselines3 library on the Atari Pong environment. The script supports command-line arguments to load pre-trained weights, continue learning after loading weights, and specify the total timesteps for training.

### requirements

- torch==2.2.2
- torchvision==0.17.2
- stable-baselines3[extra]

You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### usage

```python
python train_a2c.py [options]
```

### options

- `--load` PATH: Path to pre-trained weights. If specified, the script will load the weights from the given path.
- `--continue_training`: Continue learning after loading weights. This option is only effective when used in conjunction with `--load`.
- `--total_timesteps` STEPS: Total timesteps for training. Default is 100000.

### Example Usage

To train the model from scratch:

```bash
python train_a2c.py
```

To load pre-trained weights and continue learning for an additional 500000 timesteps:

```bash
python train_a2c.py --load  --continue_training --total_timesteps 500000
```

### File Structure

- `train_a2c.py`: Main Python script for training the A2C model.
- `model/` : Directory to save trained model weights.
- `play_pong_using_model.py` : use the pretrained model to play the game.

