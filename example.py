import Bitget_api.mix.account_api as account
import Bitget_api.mix.order_api as order
from config import *


## Account api(api/mix/v1/account/x)
# account_api = account.AccountApi(apikey, secretkey, passphrase)

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

## Order api(api/mix/v1/order/x)
order_api = order.OrderApi(apikey, secretkey, passphrase)

# res = order_api.placeOrder("BTCUSDT_UMCBL", "USDT", "0.01", "open_long", "limit", "458888", "1660", "normal", False, "1690", "1600")
# print(res)

# res = order_api.batch_orders("BTCUSDT_UMCBL", "USDT", [{"size":"0.01", "side": "open_long", "orderType": "limit","price": "1660","presetTakeProfitPrice": "1690","presetStopLossPrice": "1600"}, {"size":"0.01", "side": "open_long", "orderType": "market"}])
# print(res)

# res = order_api.cancel_orders("BTCUSDT_UMCBL", "USDT", orderId="1077089431955030016")
# print(res)

# res = order_api.cancel_batch_orders("BTCUSDT_UMCBL", "USDT", orderIds = ["1077085840435429376", "1077090639629369344"])
# print(res)

# res = order_api.modifyOrder("BTCUSDT_UMCBL", "1077090639629369344", size=0.01, presetTakeProfitPrice=1977)
# print(res)

# res = order_api.cancel_symbol_orders("BTCUSDT_UMCBL", "USDT")
# print(res)

# res = order_api.cancel_all_orders("umcbl", "USDT")
# print(res)

# res = order_api.cancel_all_positions("umcbl")
# print(res)

# res = order_api.current("BTCUSDT_UMCBL")
# print(res)

# res = order_api.marginCoinCurrent("umcbl", "USDT")
# print(res)

# res = order_api.history("BTCUSDT_UMCBL", "1692514149953", "1692529372089", "20")
# print(res)

# res = order_api.historyProductType("umcbl", "1692514149953", "1692529372089", "20")
# print(res)

# res = order_api.detail("BTCUSDT_UMCBL", clientOid="465213854")
# print(res)

# res = order_api.fills("BTCUSDT_UMCBL", startTime="1692514149953", endTime="1692529372089")
# print(res)

# res = order_api.allFills("umcbl", startTime="1692514149953", endTime="1692529372089")
# print(res)