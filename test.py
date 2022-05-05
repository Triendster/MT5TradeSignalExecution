import MetaTrader5 as mt5
import constants
import random

if not mt5.initialize():
    print('initialize() fehlgeschlagen, Fehlercode =', mt5.last_error())
    quit()

request = {
    'action'        : mt5.TRADE_ACTION_DEAL,
    'symbol'        : 'LTCBTC',
    'type'          : mt5.ORDER_TYPE_SELL,
    'price'         : mt5.symbol_info_tick('LTCBTC').bid,
    'volume'        : mt5.symbol_info('LTCBTC').volume_min,
    'deviation'     : constants.DEVIATION,
    'type_time'     : mt5.ORDER_TIME_GTC,
    'type_filling'  : mt5.ORDER_FILLING_FOK,
    'magic'         : random.randint(0, 100000),
    'sl'            : 0.0,
    'tp'            : 0.0,
    'comment'       : 'some comment',
    'position'      : 9476065,
}

for key in request.keys():
    print("{} : {}".format(key, request[key]))


result = mt5.order_send(request)
