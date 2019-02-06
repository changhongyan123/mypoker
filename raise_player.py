from pypokerengine.players import BasePokerPlayer
from time import sleep
import pprint

class RaisedPlayer(BasePokerPlayer):

  def declare_action(self, valid_actions, hole_card, round_state):
    pp = pprint.PrettyPrinter(indent=2)
    print("------------ROUND_STATE(RAISED)--------")
    #pp.pprint(round_state)
    #print("------------HOLE_CARD----------")
    #pp.pprint(hole_card)
    #print("------------VALID_ACTIONS----------")
    #pp.pprint(valid_actions)
    #print("-------------------------------")
    sleep(1)
    for i in valid_actions:
        if i["action"] == "raise":
            action, amount = i["action"], i["amount"]
            #input("RAISED->>>")
            return action, amount  # action returned here is sent to the poker engine
    action, amount = valid_actions[1]["action"], valid_actions[1]["amount"]
    return action, amount  # action returned here is sent to the poker engine

  def receive_game_start_message(self, game_info):
    pass

  def receive_round_start_message(self, round_count, hole_card, seats):
    pass

  def receive_street_start_message(self, street, round_state):
    pass

  def receive_game_update_message(self, action, round_state):
    pass

  def receive_round_result_message(self, winners, hand_info, round_state):
    pass

def setup_ai():
  return RandomPlayer()
