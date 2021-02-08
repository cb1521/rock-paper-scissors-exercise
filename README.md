# Instructions

This is a python version of a rock paper scissors game. Some set up is required in order to run the game properly.

## Set-up

First, you need to create and activate a specific Anaconda environment. Do so through the following method in the command line:

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

Once the environment is set up, you will then need to install certain packages. Do so by executing the following code, also in the command line:

```sh
pip install -r requirements.txt
```

Once these packages are installed, create a new file titled .env in the root directory of the repository, and write the following code, substituting Player One with whatever name you desire:

    USER_NAME="Player 1"

## Usage

Start the program by putting the following command into the command line:

```py
python game.py
```

Then you should be able to run the program. If there are any errors, please make sure that you set up both the environment and the external packages correctly.