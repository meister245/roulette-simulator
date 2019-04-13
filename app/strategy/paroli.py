class StrategyParoli(object):
    def __init__(self):
        pass

    @staticmethod
    def get_new_bet(bet, bet_result, table_limit=150.0):
        if bet['type'] in bet_result['win_types']:

            if bet['size_current'] * 2 > table_limit:
                return bet['size_current']

            else:
                return bet['size_current'] * 2

        else:
            return bet['size_original']

    @staticmethod
    def get_new_status(bet, bet_result):
        return True if bet['type'] in bet_result['win_types'] else False
