## Term Project

### Set up environment
using the conda or pyenv

- conda create -n cs3243 python=2.7
- conda env remove --name cs3243
- source activate cs3243

replace the cs3243 with whatever name you want
https://conda.io/docs/index.html

pip install PyPokerEngine  
https://ishikota.github.io/PyPokerEngine/



testing installmement:

```
import pypokerengine   
print("hello world")
```


### Set up gui  
```pip install pypokergui```
run the command and replace the yaml file path
```
pypokergui serve /Users/ishikota/poker/poker_conf.yaml --port 8000 --speed moderate
```


### Create your own player
#### Example

```

class RaisedPlayer(BasePokerPlayer):

  def declare_action(self, valid_actions, hole_card, round_state):
    #Implement your stragy code 
    return action, amount  #Note: modify the action and amount is not allowed here.

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
```

#### Information for the game
```valid_actions```: vaild action list


```
[
    { "action" : "fold" , "amount" : int },
    { "action" : "call" , "amount" : int },
    { "action" : "raise", "amount" : int }
]
OR 
[
    {"action": "fold", "amount": int},
    {"action": "call", "amount": int}
]
```

In the limited version, user only allowed to raise for four time in one round game.    
In addition, in each street (preflop,flop,turn,river),only allowed to raise for four times.

Other information is similar to the PyPokerEngine,please check the detail about the parameter [link](https://github.com/ishikota/PyPokerEngine/blob/master/AI_CALLBACK_FORMAT.md)