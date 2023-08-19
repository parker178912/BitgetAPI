import Bitget_api.mix.account_api as account
from config import *


account_api = account.AccountApi(apikey, secretkey, passphrase)

# res = account_api.account(symbol = 'BTCUSDT_UMCBL', marginCoin = 'USDT')
# print(res)

# res = account_api.setLeverage("ETHUSDT_UMCBL", "USDT", "50", "short")
# print(res)

# res = account_api.setMarginMode("ETHUSDT_UMCBL", "USDT", "fixed")
# print(res)