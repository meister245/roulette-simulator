from app.bet.common import BetCommon


class BetMartingale(BetCommon):
    def __init__(self, **kwargs):
        BetCommon.__init__(self, **kwargs)

    def update_bet_size(self, result, **kwargs):
        table_limit = kwargs.get('table_limit', 150.0)

        if result['win']:
            self.size_current = self.size_original

        elif not result['win'] and self.size_current * len(self.types) + 1 <= table_limit:
            self.size_current *= len(self.types) + 1

        elif not result['win'] and self.size_current * len(self.types) + 1 > table_limit:
            pass
