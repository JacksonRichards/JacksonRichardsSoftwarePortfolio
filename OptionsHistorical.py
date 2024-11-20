

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


PAPER = True
TRADE_API_URL="https://paper-api.alpaca.markets"
TRADE_API_KEY="XXXXX"
TRADE_API_SECRET="XXXXXX"

#### We use paper environment for this example ####

api_key = TRADE_API_KEY
secret_key = TRADE_API_SECRET
data_api_url = None

option_historical_data_client = OptionHistoricalDataClient(api_key, secret_key, url_override = data_api_url)
trade_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=PAPER, url_override=TRADE_API_URL)

req = OptionChainRequest(
    underlying_symbol = 'AAPL',
    type = 'call',
    expiration_date = '2024-11-08',
    strike_price_gte = '0',
)
#print(len(option_historical_data_client.get_option_chain(req)))
#print('-------------------')

res = option_historical_data_client.get_option_chain(req)
#print(res)

list_of_keys = list(res.keys())
#print(list_of_keys[0])
#print(type(res[list_of_keys[0]]))
#print(res[list_of_keys[0]])
#print(res[list_of_keys[0]].symbol)

#list_of_values = list(res.values())
#print(list_of_values[0].latest_trade)
#print(type(list_of_values[0]))


for items_keys in list_of_keys:
    option_details = res[items_keys]
    snapshot_list = list(option_details.__dict__.values())
    contract_symbol = snapshot_list[-3].symbol
    print('Contract Symbol:', contract_symbol)
    bid_price_opt = float(snapshot_list[-3].bid_price)
    print('Bid Price:', bid_price_opt)
    ask_price_opt = float(snapshot_list[-3].ask_price)
    print('Ask Price:', ask_price_opt)
    total_price_spread_opt = ask_price_opt-bid_price_opt
    print('Total Spread', total_price_spread_opt)
    print('-----------------------------------------------')
