class Stock:

    def __init__(self,l_code, l_shares, l_cost_per_share):

        #following will come in from portfolio value
        self.code = l_code
        self.shares = l_shares
        self.cost_per_share= l_cost_per_share

        #following i will get from API
        self.current_price = 0.0

        # following portfolio will be computed
        self.profit_or_loss = 0.0
        self.total_current_value = 0.0
        self.total_cost = 0.0
