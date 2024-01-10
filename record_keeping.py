

from timeit import default_timer as timer 
import time
from datetime import datetime
import pandas as pd
import csv
import numpy as np
import math
import time
from numpy import inf
import numpy as np
from timeit import default_timer as timer
import decimal
import random
import schedule
import timeit
from itertools import zip_longest
from datetime import date
from datetime import timedelta
from datetime import date
import calendar
import warnings
import datetime
import urllib.request
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest


warnings.filterwarnings('ignore')

api_keys_csv = pd.read_csv('alpaca_api_information.csv')

#paper_tf = pd.read_csv('paper_true_false.csv')

trading_client = TradingClient(api_keys_csv['API KEY'][0], api_keys_csv['API SECRET KEY'][0], paper=api_keys_csv['Portfolio Type'][0])


print("RECORD KEEPING COMMENCING")


while True:

    try:
        
        def record_keeping():
            
            
            today = date.today()
            #print("Today is: ", today)           
            # Yesterday date
            curr_date = date.today()
        
            #print(calendar.day_name[curr_date.weekday()])
        
        
        
            today_initial_data = date.today()
            y = today_initial_data.strftime("%Y-%m-%d")
            #y =  dt.strftime("%m-%d %H:%M")
            #print(x)
            #print(y)
            NY = 'America/los_angeles'
            end=pd.Timestamp(y, tz=NY)
            #print(end)       
            record_date = y
            #record_date = time_string_initial_data.replace('0', '')
            ####print("Current Day:", record_date)
        
            '''
            portfolio = api.list_positions()
            #print(portfolio)
            
            
            
            portfolio_ticker_append = []
            portfolio_qty_append = []
            portfolio_avg_entry_append = []
            portfolio_cost_basis_append = []
            portfolio_market_value_append = []
            portfolio_unrealized_pl_append = []
            portfolio_unrealized_plpc_append = []
            for items in portfolio:
                portfolio_ticker = items.symbol
                ####print("portfolio_ticker:", portfolio_ticker)
                portfolio_ticker_append.append(portfolio_ticker)
                
                portfolio_qty = items.qty
                ####print("portfolio_qty:", portfolio_qty)
                portfolio_qty_append.append(portfolio_qty)
                
                portfolio_avg_entry = items.avg_entry_price
                ####print("portfolio_avg_entry:", portfolio_avg_entry)
                portfolio_avg_entry_append.append(portfolio_avg_entry)
                
                portfolio_cost_basis = items.cost_basis
                ####print("portfolio_cost_basis:", portfolio_cost_basis)
                portfolio_cost_basis_append.append(portfolio_cost_basis)
                
                portfolio_market_value = items.market_value
                ####print("portfolio_market_value:", portfolio_market_value)
                portfolio_market_value_append.append(portfolio_market_value)
                
                portfolio_unrealized_pl = items.unrealized_pl
                ####print("portfolio_unrealized_pl:", portfolio_unrealized_pl)
                portfolio_unrealized_pl_append.append(portfolio_unrealized_pl)
                
                portfolio_unrealized_plpc = items.unrealized_plpc
                ####print("portfolio_unrealized_plpc:", portfolio_unrealized_plpc)
                portfolio_unrealized_plpc_append.append(portfolio_unrealized_plpc)
                
                ####print('-----------------------')
                
            record_one = pd.DataFrame(portfolio_ticker_append)
            record_two = pd.DataFrame(portfolio_qty_append)
            record_three = pd.DataFrame(portfolio_avg_entry_append)
            record_four = pd.DataFrame(portfolio_cost_basis_append)
            record_five = pd.DataFrame(portfolio_market_value_append)
            record_six = pd.DataFrame(portfolio_unrealized_pl_append)
            record_seven = pd.DataFrame(portfolio_unrealized_plpc_append)
            
            records_df = pd.concat([record_one, record_two, record_three, record_four, record_five, record_six, record_seven], axis = 1)
            records_df.columns =['Ticker','Shares','Average Entry Price','Cost Basis','MArket Value','Profit/Loss','Profit/Loss Percentage']
            
            stock_positions = pd.DataFrame(records_df)
            #print(stock_positions)
            
            stock_positions.to_csv('stock_positions.csv')
            
            ####print('-----------------------')
            '''
            
            
            
            
            
            
            account = trading_client.get_account()
            #print(account)
            
            account_blocked_append = []
            account_number_append = []
            accrued_fees_append = []
            buying_power_append = []
            cash_append = []
            created_at_append = []
            crypto_status_append = []
            currency_append = []
            daytrade_count_append = []
            daytrading_buying_power_append = []
            equity_append = []
            id_append = []
            initial_margin_append = []
            last_equity_append = []
            last_maintenance_margin_append = []
            long_market_value_append = []
            maintenance_margin_append = []
            multiplier_append = []
            non_marginable_buying_power_append = []
            pattern_day_trader_append = []
            pending_transfer_in_append = []
            portfolio_value_append = []
            regt_buying_power_append = []
            short_market_value_append = []
            shorting_enabled_append = []
            sma_append = []
            status_append = []
            trade_suspended_by_user_append = []
            trading_blocked_append = []
            transfers_blocked_append = []
            
            account_blocked = account.account_blocked
            ####print("account_blocked:", account_blocked)
            account_blocked_append.append(account_blocked)
            
            account_number = account.account_number
            ####print("account_number:", account_number)
            account_number_append.append(account_number)
            
            accrued_fees = account.accrued_fees
            ####print("accrued_fees:", accrued_fees)
            accrued_fees_append.append(accrued_fees)
            
            buying_power = account.buying_power
            ####print("buying_power:", buying_power)
            buying_power_append.append(buying_power)
            
            cash = account.cash
            ####print("cash:", cash)
            cash_append.append(cash)
            
            created_at = account.created_at
            ####print("created_at:", created_at)
            created_at_append.append(created_at)
            
            crypto_status = account.crypto_status
            ####print("crypto_status:", crypto_status)
            crypto_status_append.append(crypto_status)
            
            currency = account.currency
            ####print("currency:", currency)
            currency_append.append(currency)
            
            daytrade_count = account.daytrade_count
            ####print("daytrade_count:", daytrade_count)
            daytrade_count_append.append(daytrade_count)
            
            daytrading_buying_power = account.daytrading_buying_power
            ####print("daytrading_buying_power:", daytrading_buying_power)
            daytrading_buying_power_append.append(daytrading_buying_power)
            
            equity = account.equity
            ####print("equity:", equity)
            equity_append.append(equity)
            
            ids = account.id
            ####print("ids:", ids)
            id_append.append(ids)
            
            initial_margin = account.initial_margin
            ####print("initial_margin:", initial_margin)
            initial_margin_append.append(initial_margin)
            
            last_equity = account.last_equity
            ####print("last_equity:", last_equity)
            last_equity_append.append(last_equity)
            
            last_maintenance_margin = account.last_maintenance_margin
            ####print("last_maintenance_margin:", last_maintenance_margin)
            last_maintenance_margin_append.append(last_maintenance_margin)
            
            long_market_value = account.long_market_value
            ####print("long_market_value:", long_market_value)
            long_market_value_append.append(long_market_value)
            
            maintenance_margin = account.maintenance_margin
            ####print("maintenance_margin:", maintenance_margin)
            maintenance_margin_append.append(maintenance_margin)
            
            multiplier = account.multiplier
            ####print("multiplier:", multiplier)
            multiplier_append.append(multiplier)
            
            non_marginable_buying_power = account.non_marginable_buying_power
            ####print("non_marginable_buying_power:", non_marginable_buying_power)
            non_marginable_buying_power_append.append(non_marginable_buying_power)
            
            pattern_day_trader = account.pattern_day_trader
            ####print("pattern_day_trader:", pattern_day_trader)
            pattern_day_trader_append.append(pattern_day_trader)
            
            pending_transfer_in = account.pending_transfer_in
            ####print("pending_transfer_in:", pending_transfer_in)
            pending_transfer_in_append.append(pending_transfer_in)
            
            portfolio_value = account.portfolio_value
            ####print("portfolio_value:", portfolio_value)
            portfolio_value_append.append(portfolio_value)
            
            regt_buying_power = account.regt_buying_power
            ####print("regt_buying_power:", regt_buying_power)
            regt_buying_power_append.append(regt_buying_power)
            
            short_market_value = account.short_market_value
            ####print("short_market_value:", short_market_value)
            short_market_value_append.append(short_market_value)
            
            shorting_enabled = account.shorting_enabled
            ####print("shorting_enabled:", shorting_enabled)
            shorting_enabled_append.append(shorting_enabled)
            
            sma = account.sma
            ####print("sma:", sma)
            sma_append.append(sma)
            
            status = account.status
            ####print("status:", status)
            status_append.append(status)
            
            trade_suspended_by_user = account.trade_suspended_by_user
            ####print("trade_suspended_by_user:", trade_suspended_by_user)
            trade_suspended_by_user_append.append(trade_suspended_by_user)
            
            trading_blocked = account.trading_blocked
            ####print("trading_blocked:", trading_blocked)
            trading_blocked_append.append(trading_blocked)
            
            transfers_blocked = account.transfers_blocked
            ####print("transfers_blocked:", transfers_blocked)
            transfers_blocked_append.append(transfers_blocked)
                
            ####print('-----------------------')
            
            record_one = pd.DataFrame(account_blocked_append)
            record_two = pd.DataFrame(account_number_append)
            record_three = pd.DataFrame(accrued_fees_append)
            record_four = pd.DataFrame(buying_power_append)
            record_five = pd.DataFrame(cash_append)
            record_six = pd.DataFrame(created_at_append)
            record_eight = pd.DataFrame(crypto_status_append)
            record_nine = pd.DataFrame(currency_append)
            record_ten = pd.DataFrame(daytrade_count_append)
            record_eleven = pd.DataFrame(daytrading_buying_power_append)
            record_twelve = pd.DataFrame(equity_append)
            record_thirteen = pd.DataFrame(id_append)
            record_fourteen = pd.DataFrame(initial_margin_append)
            record_fifteen = pd.DataFrame(last_equity_append)
            record_sixteen = pd.DataFrame(last_maintenance_margin_append)
            record_seventeen = pd.DataFrame(long_market_value_append)
            record_eighteen = pd.DataFrame(maintenance_margin_append)
            record_nineteen = pd.DataFrame(multiplier_append)
            record_twenty = pd.DataFrame(non_marginable_buying_power_append)
            record_twentyone = pd.DataFrame(pattern_day_trader_append)
            record_twentytwo = pd.DataFrame(pending_transfer_in_append)
            record_twentythree = pd.DataFrame(portfolio_value_append)
            record_twentyfour = pd.DataFrame(regt_buying_power_append)
            record_twentyfive = pd.DataFrame(short_market_value_append)
            record_twentysix = pd.DataFrame(shorting_enabled_append)
            record_twentyseven = pd.DataFrame(sma_append)
            record_twentyeight = pd.DataFrame(status_append)
            record_twentynine = pd.DataFrame(trade_suspended_by_user_append)
            record_thirty = pd.DataFrame(trading_blocked_append)
            record_thirtyone = pd.DataFrame(transfers_blocked_append)
            
            
            records_stock_activites_margin_requirements_df = pd.concat([record_one,record_two,record_three,record_four,record_five,record_six,record_eight,record_nine,record_ten,
                                                                        record_eleven,record_twelve,record_thirteen,record_fourteen,record_fifteen,record_sixteen,record_seventeen,
                                                                        record_eighteen,record_nineteen,record_twenty,record_twentyone,record_twentytwo,record_twentythree,record_twentyfour,
                                                                        record_twentyfive,record_twentysix,record_twentyseven,record_twentyeight,record_twentynine,record_thirty,record_thirtyone], axis = 1)
            #print(records_stock_activites_margin_requirements_df)
            records_stock_activites_margin_requirements_df.columns = ['account_blocked','account_number','accrued_fees','buying_power','cash','created_at','crypto_status','currency',
                                                                     'daytrade_count','daytrading_buying_power','equity','ids','initial_margin','last_equity',
                                                                     'last_maintenance_margin','long_market_value','maintenance_margin',
                                                                     'multiplier','non_marginable_buying_power','pattern_day_trader','pending_transfer_in','portfolio_value',
                                                                     'regt_buying_power','short_market_value','shorting_enabled',
                                                                     'sma','status','trade_suspended_by_user','trading_blocked','transfers_blocked']
            
            stock_activites_margin_requirements = pd.DataFrame(records_stock_activites_margin_requirements_df)
            #print(stock_positions)
            
            stock_activites_margin_requirements.to_csv('stock_balance_marginrequirements.csv') 
            
            ####print('-----------------------')
            
            '''
            trade_history = api.get_portfolio_history(date_start=record_date, date_end=record_date, extended_hours=True).df
            pd.set_option('display.max_rows', 100)
            #print(trade_history.df)
            trade_history.to_csv('portfolio_data.csv')
            ####print(trade_history)
            '''
            
            ####print('-----------------------')
            
            
            
            request_params = GetOrdersRequest(status='closed', date=record_date)
            #print(request_params)

            # orders that satisfy params
            activity = trading_client.get_orders(filter=request_params)
            #print(activity)
            #print(activity[0])
        
        
            activity_type_append = []
            cum_qty_append = []
            id_append = []
            leaves_qty_append = []
            order_id_append = []
            order_status_append = []
            price_append = []
            qty_append = []
            side_append = []
            symbol_append = []
            transaction_time_append = []
            type_append = []
        
        
            for items in activity:
                
                activity_type = items.status
                #print("activity_type:", activity_type)
                activity_type_append.append(activity_type)
        
                cum_qty = items.filled_qty
                #print("activity_type:", activity_type)
                cum_qty_append.append(cum_qty)
                
                ids = items.id
                #print("activity_type:", activity_type)
                id_append.append(ids)
                
                order_id = items.client_order_id
                #print("activity_type:", activity_type)
                order_id_append.append(order_id)
                
                order_status = items.status
                #print("activity_type:", activity_type)
                order_status_append.append(order_status)
                
                price = items.filled_avg_price
                #print("activity_type:", activity_type)
                price_append.append(price)
                
                qty = items.qty
                #print("activity_type:", activity_type)
                qty_append.append(qty)
                
                side = items.side
                #print("activity_type:", activity_type)
                side_append.append(side)
                
                symbol = items.symbol
                #print("activity_type:", activity_type)
                symbol_append.append(symbol)
                
                transaction_time = items.created_at
                #print(transaction_time)
                transaction_time = transaction_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
                #print(transaction_time)
                NY = 'America/los_angeles'
                transaction_time=pd.Timestamp(transaction_time, tz=NY)
                #print(end)       
                #print(transaction_time)
                
                transaction_time_append.append(transaction_time)
        
                
                
                types = items.type
                #print("activity_type:", activity_type)
                type_append.append(types)
                
            #print(transaction_time_append)
            #print(type(transaction_time_append))
            
        
            
        
            record_one = pd.DataFrame(activity_type_append)
            record_two = pd.DataFrame(cum_qty_append)
            record_three = pd.DataFrame(id_append)
            record_five = pd.DataFrame(order_id_append)
            record_six = pd.DataFrame(order_status_append)
            record_eight = pd.DataFrame(price_append)
            record_nine = pd.DataFrame(qty_append)
            record_ten = pd.DataFrame(side_append)
            record_eleven = pd.DataFrame(symbol_append)
            record_twelve = pd.DataFrame(transaction_time_append)
            record_thirteen = pd.DataFrame(type_append)
        
        
        
            records_stock_activities = pd.concat([record_one,record_two,record_three,record_five,record_six,record_eight,record_nine,record_ten,
                                                                        record_eleven,record_twelve,record_thirteen], axis = 1)
        
        
            records_stock_activities.columns = ['activity_type','cum_qty','id','order_id','order_status','price','qty',
                                                                     'side','symbol','transaction_time','type']
        
            records_stock_activities_df = pd.DataFrame(records_stock_activities)
            #print(stock_positions)
        
            records_stock_activities_df.to_csv('stock_activities.csv') 
        
            ####print('-----------------------')   
            ####print('-----------------------')
            
            print("RECORD KEEPING COMPLETE")   
            
        record_keeping()    
    
        break
    
    except:
        
        print("No Internet Connection, Attempting Reconnection... - Record Keeping")
        time.sleep(0.5)












