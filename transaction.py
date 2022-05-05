import constants
import MetaTrader5 as mt5
import json
import os
import random

def init_MT5():
    if not mt5.initialize():
        print('initialize() fehlgeschlagen, Fehlercode =', mt5.last_error())
        quit()


class Transaction:
    '''Enthält alle zur Transaktion nötigen Daten, generiert Anfragen, führt diese durch und gibt Resultat an Nutzer'''
    def __init__(self, filepath):
        with open(filepath, 'r') as readSignal:
            self.signal    = json.load(readSignal)
        self.action        = mt5.TRADE_ACTION_SLTP if self.signal['type'] == constants.CHANGE_SLTP else mt5.TRADE_ACTION_DEAL
        self.comment       = self.signal['send_id']
        self.symbol        = self.signal['symbol']
        self.magic         = random.randint(0, 100000)
        if self.signal['type'] == constants.CHANGE_SLTP or self.signal['type'] == constants.CLOSE:
            self.type      = self.signal['otype']
        else:
            self.type      = constants.ORDER_TYPE[self.signal['type']]
        if self.signal['type'] == constants.CHANGE_SLTP:
            self.sltp      = (self.signal['sl'], self.signal['tp'])
        self.trade_request = self.create_trade_request()
        self.allow         = True

    def check_open_positions(self):
        '''Falls Schließen oder Ändern von SLTP'''
        open_positions = mt5.positions_get(symbol=self.symbol)
        if not open_positions:
            self.message = constants.NO_POSITION_FOUND.format(self.symbol, self.comment)
            self.allow   = False
        else:
            # Falls mehrere Positionen gleichen Symbols, suche über send_id
            for op in open_positions:
                if op.comment == self.comment:
                    self.position = op.ticket

    def create_trade_request(self):
        '''Erstellt Handelsanfrage-Objekt'''
        init_MT5()
        if self.signal['type'] == constants.CLOSE or self.signal['type'] == constants.CHANGE_SLTP:
            self.check_open_positions()
        request = {
            'action'        : self.action,
            'symbol'        : self.symbol,
            'volume'        : mt5.symbol_info(self.symbol).volume_min,
            'type'          : self.type,
            'price'         : mt5.symbol_info_tick(self.symbol).ask if self.type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(self.symbol).bid,
            'deviation'     : constants.DEVIATION,
            'magic'         : self.magic,
            'comment'       : self.comment,
            'type_time'     : mt5.ORDER_TIME_GTC,
            'type_filling'  : mt5.ORDER_FILLING_FOK,
            'sl'            : self.sltp[0] if hasattr(self, 'sltp') else 0.0,
            'tp'            : self.sltp[1] if hasattr(self, 'sltp') else 0.0,
        }
        if hasattr(self, 'position'):
            request['position'] = self.position
        return request

    def execute_trade(self):
        '''Führe Handelsanfrage durch'''
        if not self.allow:
            return
        init_MT5()
        for key in self.trade_request.keys():
            print("{} : {}".format(key, self.trade_request[key]))
        result = mt5.order_send(self.trade_request)
        if not result:
            self.message = constants.NO_TRADE_RESULT.format(self.symbol, self.comment)
        else:
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                self.message = constants.TRADE_FAILED.format(self.symbol, self.comment, str(result.retcode), constants.RETCODES[str(result.retcode)])
            else:
                m_list = []
                result_dict = result._asdict()
                for key in result_dict.keys():
                    m_list.append("{} : {}".format(key, result_dict[key]))
                self.message = constants.TRADE_SUCCESS.format("\n".join(m_list))
