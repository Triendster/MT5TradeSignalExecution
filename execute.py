import signalclient
import transaction
import logging
import os
import datetime


try:
    client = signalclient.SignalClient()
    filepath = signalclient.run_get_signal()

    if not filepath:
        pass
    else:
        transaction = transaction.Transaction(filepath)
        transaction.execute_trade()
        client.send_message(transaction.message)

except Exception as Argument:
    filename = os.path.join(os.getcwd(), constants.LOGS, datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")[:-3] + constants.LOG)
    print(Argument)
    with open(filename, 'w') as errorFile:
        errorFile.write(str(Argument))
