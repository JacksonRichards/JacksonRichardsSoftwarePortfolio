

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from alpaca.trading.client import TradingClient
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical.option import OptionHistoricalDataClient
from alpaca.trading.stream import TradingStream
from alpaca.data.live.option import OptionDataStream
import pandas as pd
from alpaca.data.requests import (
    OptionBarsRequest,
    OptionTradesRequest,
    OptionLatestQuoteRequest,
    OptionLatestTradeRequest,
    OptionSnapshotRequest,
    OptionChainRequest    
)
from alpaca.trading.requests import (
    GetOptionContractsRequest,
    GetAssetsRequest,
    MarketOrderRequest,
    GetOrdersRequest,
    ClosePositionRequest
)
from alpaca.trading.enums import (
    AssetStatus,
    ExerciseStyle,
    OrderSide,
    OrderType,
    TimeInForce,
    QueryOrderStatus 
)
from alpaca.common.exceptions import APIError


TRADE_API_KEY="XXXXX"
TRADE_API_SECRET="XXXXX"

#### We use paper environment for this example ####
PAPER=True
TRADE_API_URL="https://paper-api.alpaca.markets"
TRADE_API_WSS=None
DATA_API_URL=None
OPTION_STREAM_DATA_WSS=None

api_key = TRADE_API_KEY
secret_key = TRADE_API_SECRET
paper = PAPER
trade_api_url = TRADE_API_URL

trade_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=paper, url_override=trade_api_url)
option_historical_data_client = OptionHistoricalDataClient(api_key, secret_key, url_override=None)

underlying_symbol = "AAPL"

# specify expiration date range
now = datetime.now(tz=ZoneInfo("America/Los_Angeles"))
day1 = now + timedelta(days=1)
day60 = now + timedelta(days=1)
#print(day60)


req = GetOptionContractsRequest(
    underlying_symbol=[underlying_symbol],                 
# specify underlying symbol
    status=AssetStatus.ACTIVE,                           
# specify asset status: active (default)
    expiration_date=None,                                
# specify expiration date (specified date + 1 day range)
    ##expiration_date_gte=day1.date(),                        
# we can pass date object
    expiration_date_lte=day60.strftime(format="%Y-%m-%d"),  
# or string
    root_symbol=underlying_symbol,                                    
# specify root symbol
    type="call",                                          
# specify option type: put
    style=ExerciseStyle.AMERICAN,                        
# specify option style: american
    strike_price_gte=None,                               
# specify strike price range
    strike_price_lte=None,                               
# specify strike price range
    limit=10000,                                           
# specify limit
    page=None,                                           
# specify page
)
res = trade_client.get_option_contracts(req)
#print(res)


new_format = "%Y-%m-%d"
new_datetime_str = day60.strftime(new_format)

req_bid_ask = OptionChainRequest(
    underlying_symbol = underlying_symbol,
    type = 'call',
    expiration_date = new_datetime_str,
    strike_price_gte = '0',
)
res_bid_ask = option_historical_data_client.get_option_chain(req_bid_ask)
list_of_keys = list(res_bid_ask.keys())

bid_price_append = []
ask_price_append = []
spread_append = []
for items_keys in list_of_keys:
    option_details = res_bid_ask[items_keys]
    snapshot_list = list(option_details.__dict__.values())
    contract_symbol = snapshot_list[-3].symbol
    #print('Contract Symbol:', contract_symbol)
    bid_price_opt = float(snapshot_list[-3].bid_price)
    bid_price_append.append(bid_price_opt)
    ask_price_opt = float(snapshot_list[-3].ask_price)
    ask_price_append.append(ask_price_opt)
    total_price_spread_opt = ask_price_opt-bid_price_opt
    spread_append.append(total_price_spread_opt)
    

#symbol = res.option_contracts[0].symbol
#contract = trade_client.get_option_contract(symbol)
#print(contract)

id_append = []
symbol_append = []
name_append = []
status_append = []
tradeable_append = []
exp_date_append = []
root_symbol_append = []
underlying_symbol_append = []
underlying_asset_id_append = []
option_type_append = []
style_append = []
strike_price_append = []
size_append = []
open_interest_append = []
open_interest_date_append = []
bid_price_final_append = []
ask_price_final_append = []
spread_price_final_append = []
close_price_append = []
close_price_date_append = []
for items in res.option_contracts:
    id = items.id
    id_append.append(id)

    symbol = items.symbol
    symbol_append.append(symbol)

    name = items.name
    name_append.append(name)

    status = items.status
    status_append.append(status)

    tradeable = items.tradable
    tradeable_append.append(tradeable)

    exp_date = items.expiration_date
    exp_date_append.append(exp_date)

    root_symbol = items.root_symbol
    root_symbol_append.append(root_symbol)

    underlying_symbol = items.underlying_symbol
    underlying_symbol_append.append(underlying_symbol)

    underlying_asset_id = items.underlying_asset_id
    underlying_asset_id_append.append(underlying_asset_id)

    option_type = items.type
    option_type_append.append(option_type)

    style = items.style
    style_append.append(style)
    
    strike_price = items.strike_price
    strike_price_append.append(strike_price)

    size = items.size
    size_append.append(size)

    open_interest = items.open_interest
    open_interest_append.append(open_interest)

    open_interest_date = items.open_interest_date
    open_interest_date_append.append(open_interest_date)


    symbol_location = list_of_keys.index(symbol)

    bid_price_temp = bid_price_append[symbol_location]
    bid_price_final_append.append(bid_price_temp)

    ask_price_temp = ask_price_append[symbol_location]
    ask_price_final_append.append(ask_price_temp)

    spread_price_temp = spread_append[symbol_location]
    spread_price_final_append.append(spread_price_temp)
    

    close_price = items.close_price
    close_price_append.append(close_price)

    close_price_date = items.close_price_date
    close_price_date_append.append(close_price_date)





id_append_df = pd.DataFrame(id_append)
symbol_append_df = pd.DataFrame(symbol_append)
name_append_df = pd.DataFrame(name_append)
status_append_df = pd.DataFrame(status_append)
tradeable_append_df = pd.DataFrame(tradeable_append)
exp_date_append_df = pd.DataFrame(exp_date_append)
root_symbol_append_df = pd.DataFrame(root_symbol_append)
underlying_symbol_append_df = pd.DataFrame(underlying_symbol_append)
underlying_asset_id_append_df = pd.DataFrame(underlying_asset_id_append)
option_type_append_df = pd.DataFrame(option_type_append)
style_append_df = pd.DataFrame(style_append)
strike_price_append_df = pd.DataFrame(strike_price_append)
size_append_df = pd.DataFrame(size_append)
open_interest_append_df = pd.DataFrame(open_interest_append)
open_interest_date_append_df = pd.DataFrame(open_interest_date_append)
bid_price_append_df = pd.DataFrame(bid_price_final_append)
ask_price_append_df = pd.DataFrame(ask_price_final_append)
spread_price_append_df = pd.DataFrame(spread_price_final_append)
close_price_append_df = pd.DataFrame(close_price_append)
close_price_date_append_df = pd.DataFrame(close_price_date_append)

final_options_concat = pd.concat([id_append_df,
                                  symbol_append_df,
                                  name_append_df,
                                  status_append_df,
                                  tradeable_append_df,
                                  exp_date_append_df,
                                  root_symbol_append_df,
                                  underlying_symbol_append_df,
                                  underlying_asset_id_append_df,
                                  option_type_append_df,
                                  style_append_df,
                                  strike_price_append_df,
                                  size_append_df,
                                  open_interest_append_df,
                                  open_interest_date_append_df,
                                  bid_price_append_df,
                                  ask_price_append_df,
                                  spread_price_append_df,
                                  close_price_append_df,
                                  close_price_date_append_df], axis=1)

final_options_concat.columns = ['id','symbol','name','status','tradable','expiration_date','root_symbol','underlying_symbol','underlying_asset_id','type','style','strike_price','size','open_interest','open_interest_date','bid_price','ask_price','spread_price','close_price','close_price_date']
#print(final_options_concat)
final_options_concat.to_csv(underlying_symbol+'_'+new_datetime_str+'_options_information.csv')
