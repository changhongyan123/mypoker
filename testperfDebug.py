import sys
import pprint

sys.path.insert(0, './pypokerengine/api/')
import game

setup_config = game.setup_config
start_poker = game.start_poker
import time
from argparse import ArgumentParser

""" =========== *Remember to import your agent!!! =========== """
from randomplayer import RandomPlayer

# from smartwarrior import SmartWarrior
""" ========================================================= """

""" Example---To run testperf.py with random warrior AI against itself. 

$ python testperf.py -n1 "Random Warrior 1" -a1 RandomPlayer -n2 "Random Warrior 2" -a2 RandomPlayer
"""


def testperf(agent_name1, agent1, agent_name2, agent2):
    # Init to play 500 games of 1000 rounds
    num_game = 100
    max_round = 1000
    initial_stack = 10000
    smallblind_amount = 20

    # Init pot of players
    agent1_pot = 0
    agent2_pot = 0

    # Setting configuration
    config = setup_config(max_round=max_round, initial_stack=initial_stack, small_blind_amount=smallblind_amount)

    # Register players
    config.register_player(name=agent_name1, algorithm=RandomPlayer())
    config.register_player(name=agent_name2, algorithm=RandomPlayer())

    # Start playing num_game games
    for game in range(1, num_game + 1):
        print("Game number: ", game)
        game_result = start_poker(config, verbose=0)
        agent1_pot  = game_result['players'][0]['stack']
        agent2_pot  = game_result['players'][1]['stack']
        pprint.pprint(game_result)
        print("Finished Game : "+str(game)+"\n\n")
        
        if (agent1_pot+agent2_pot != 2*initial_stack):
                raise ValueError("Missing Money !!!")




def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('-n1', '--agent_name1', help="Name of agent 1", default="A", type=str)
    parser.add_argument('-a1', '--agent1', help="Agent 1", default=RandomPlayer())
    parser.add_argument('-n2', '--agent_name2', help="Name of agent 2", default="B", type=str)
    parser.add_argument('-a2', '--agent2', help="Agent 2", default=RandomPlayer())
    args = parser.parse_args()
    return args.agent_name1, args.agent1, args.agent_name2, args.agent2


if __name__ == '__main__':
    name1, agent1, name2, agent2 = parse_arguments()
    start = time.time()
    testperf(name1, agent1, name2, agent2)
    end = time.time()

    print("\n Time taken to play: %.4f seconds" % (end - start))
