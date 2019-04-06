from pypokerengine.players import BasePokerPlayer
from time import sleep
import pprint

class RaisedPlayer(BasePokerPlayer):

  def declare_action(self, valid_actions, hole_card, round_state):
    # print("Raise Player")
    # print("Valid Actions : ")
    # pprint.pprint(valid_actions)
    for i in valid_actions:
        if i["action"] == "raise":
            action = i["action"]
            # print("(R1)Taken Actions : ")
            # pprint.pprint(action)
            # action = 'raise'
            # pprint.pprint(valid_actions)
            return action  # action returned here is sent to the poker engine
    action = valid_actions[1]["action"]
    # print("(R2)Taken Actions : ")
    # pprint.pprint(action)
    # action = 'raise'
    # pprint.pprint(valid_actions)
    return action # action returned here is sent to the poker engine

  def receive_game_start_message(self, game_info):
    pass

  def receive_round_start_message(self, round_count, hole_card, seats):
    pass

  def receive_street_start_message(self, street, round_state):
    # print("Street %s Started"%street)
    # print("-------------------------------")
    # print('\n')
    pass

  def receive_game_update_message(self, action, round_state):
    pass

  def receive_round_result_message(self, winners, hand_info, round_state):
    pprint.pprint(round_state)
    # while True:
    #   pass
    print("---------------")
    #pass

def setup_ai():
  return RandomPlayer()
