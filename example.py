import Bitget_api.mix.account_api as account
from config import *

account_api = account.AccountApi(apikey, secretkey, passphrase)

# res = account_api.account(symbol = 'BTCUSDT_UMCBL', marginCoin = 'USDT')
# print(res)

# res = account_api.accounts("umcbl")
# print(res)

# res = account_api.sub_account_contract_assets("umcbl")
# print(res)

# res = account_api.open_count("BTCUSDT_UMCBL", "USDT", "23189.5", "5000", "20")
# print(res)

# res = account_api.setLeverage("BTCUSDT_UMCBL", "USDT", "50", "short")
# print(res)

# res = account_api.setMargin("BTCUSDT_UMCBL", "USDT", "10")
# print(res)

# res = account_api.setMarginMode("BTCUSDT_UMCBL", "USDT", "crossed")
# print(res)

# res = account_api.setPositionMode("umcbl", "double_hold")
# print(res)

# res = account_api.accountBill("umcbl", "USDT", "1692460690435", "1692463078776")
# print(res)

# res = account_api.accountBusinessBill("umcbl", "USDT", "1692460690435", "1692463078776")
# print(res)