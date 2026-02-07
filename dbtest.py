from DBService import DBService

DBService.execute_query('CREATE TABLE if not exists portfolios(stock_code TEXT, '
                        'share_price float, amount_of_shares integer, total_cost float, current_price float, '
                        'current_value float, profit/loss float, 52_Week_High float, Account_Percent float)')

#DBService.execute_query('ALTER TABLE portfolios ADD COLUMN IF NOT EXISTS ROI float')
#DBService.execute_query('ALTER TABLE portfolios ADD COLUMN IF NOT EXISTS portfolio_name text')
#DBService.execute_query('ALTER TABLE portfolios ADD COLUMN IF NOT EXISTS portfolio_date date')
#DBService.execute_query('ALTER TABLE portfolios ADD CONSTRAINT IF NOT EXISTS portfolios_pk PRIMARY KEY (portfolio_name, portfolio_date)')

#DBService.execute_query("INSERT INTO portfolios (stock_code, amount_of_shares, share_price, current_price, total_cost, current_value, net_gain) VALUES ('TSLA', 25, 32.0, 12.0, 250.0, 300.0, 50.0)")

