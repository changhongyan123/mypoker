from pypokerengine.engine.action_checker import ActionChecker

ACTION_CALL = "call"
ACTION_FOLD = "fold"
ACTION_RAISE = "raise"

def generate_legal_actions(players, player_position, sb_amount,street):
    return ActionChecker.legal_actions(players, player_position, sb_amount,street)

def is_legal_action(players, player_position, sb_amount, action, amount=None):
    return ActionChecker._is_legal(
            players, player_position, sb_amount, action, amount)

