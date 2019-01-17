from pypokerengine.api.game import setup_config, start_poker
from fishplayer import FishPlayer
from consoleplayer import ConsolePlayer
from randomplayer import RandomPlayer
from honestplayer import HonestPlayer



def setup_ai():
    return FishPlayer()