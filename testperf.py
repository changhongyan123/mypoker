import sys
sys.path.insert(0, './pypokerengine/api/')
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

	# Init to play 500 games of 1000 rounds
	num_game = 500
	max_round = 1000
	initial_stack = 10000
	smallblind_amount = 20

	# Init pot of players
	randplayer_pot = 0
	agentplayer_pot = 0

	# Setting configuration
	config = setup_config(max_round=max_round, initial_stack=initial_stack, small_blind_amount=smallblind_amount)
	
	# Register players
	config.register_player(name="R1", algorithm=RandomPlayer())
	config.register_player(name=agent_name, algorithm=RandomPlayer())
	

	# Start playing num_game games
	for game in range(1, num_game+1):
		print("Game number: ", game)
		game_result = start_poker(config, verbose=0)
		randplayer_pot = randplayer_pot + game_result['players'][0]['stack']
		agentplayer_pot = agentplayer_pot + game_result['players'][1]['stack']

	print("\n After playing {} games of {} rounds, the results are: ".format(num_game, max_round))
	print("\n Random player's final pot: ", randplayer_pot)
	print("\n " + agent_name + "'s final pot: ", agentplayer_pot)

	# print("\n ", game_result)
	# print("\n Random player's final stack: ", game_result['players'][0]['stack'])
	# print("\n " + agent_name + "'s final stack: ", game_result['players'][1]['stack'])

	if (randplayer_pot<agentplayer_pot):
		print("\n Congratulations! " + agent_name + " has won.")
	elif(randplayer_pot>agentplayer_pot):
		print("\n Random Player has won!")
	else:
		Print("\n Draw. Please try again") 


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