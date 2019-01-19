import sys
sys.path.insert(0, './PyPokerEngine/pypokerengine/api/')
import game
setup_config = game.setup_config
start_poker = game.start_poker
# from fishplayer import FishPlayer
from randomplayer import RandomPlayer
# from honestplayer import HonestPlayer
# from consoleplayer import ConsolePlayer

import time
from argparse import ArgumentParser

""" To run testperf.py with your random warrior AI or smart warrior AI
$ python testperf.py -n "Random Warrior" -a RandomPlayer
$ python testperf.py -n "Smart Warrior" -a smartwarrior
"""

def testperf(agent_name, agent):	

	# setup_config = game.setup_config
	# start_poker = game.start_poker

	# config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=20)
	config = setup_config(max_round=500*1000, initial_stack=10000, small_blind_amount=20)
	# config.register_player(name="F1", algorithm=FishPlayer())
	config.register_player(name="R1", algorithm=RandomPlayer())
	config.register_player(name=agent_name, algorithm=RandomPlayer())

	game_result = start_poker(config, verbose=0)

	print("\n ", game_result)

	print("\n Random player's final stack: ", game_result['players'][0]['stack'])
	print("\n " + agent_name + "'s final stack: ", game_result['players'][1]['stack'])

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('-n', '--agent_name', help="Name of your agent", default="Your agent", type=str)
    parser.add_argument('-a', '--agent', help="Your group's agent", default=RandomPlayer())    
    args = parser.parse_args()
    return args.agent_name, args.agent

if __name__ == '__main__':
	name, agent = parse_arguments()
	start = time.time()
	testperf(name, agent)
	end = time.time()
	print("\n Time taken to play: %.4f seconds" %(end-start))