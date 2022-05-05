import MetaTrader5 as mt5


# Konstanten, die dem Typ der json-Datei die richtige mt5-Order-type zuordnen
ORDER_TYPE  = {'BUY':mt5.ORDER_TYPE_BUY, 'SELL':mt5.ORDER_TYPE_SELL}
CHANGE_SLTP = 'CHANGE_SLTP'
CLOSE       = 'CLOSE'
BUY         = 'BUY'
SELL        = 'SELL'

# Konstanten, die Trade Request Standardeinstellungen betreffen
DEVIATION   = 10

# Konstanten, die das zur Anwendung gehörige Dateisystem betreffen
SIGNALS    = 'signals'
LOGS       = 'logs'
LOG        = '.log'

# Konstanten zur Konfiguration
CONFIG     = 'config.ini'
RUN        = 'execute.py'

# Konstanten die Telethon verwendet
TELEGRAM_JSON = 'application/json'

# Konstanten, die Nachrichten betreffen werden, die bei Eingang von Signalen und Durchführung der Transaktionen versendet werden
NO_POSITION_FOUND = 'Es wurde keine offene Position zum Symbol {0} und der ID {1} gefunden.'
NO_TRADE_RESULT   = 'Es konnte kein Handelsresultat zum Symbol {0} und der ID {1} erzeugt werden.'
TRADE_FAILED      = 'Es konnte keine Position zum Symbol {0} und der ID {1} eröffnet werden. Retcode: {2}\n{3}'
TRADE_SUCCESS     = 'Resultat der erfolgreichen Handelsposition:\n\n{0}'

# Wiedergabecodes der Resultate:
RETCODES = {
      "10004": "Requote",
      "10006": "Anforderung ist abgelehnt ",
      "10007": "Anforderung ist vom Trader aufgehoben ",
      "10008": "Order ist platziert ",
      "10009": "Anforderung ist erf\u00fcllt ",
      "10010": "Anforderung ist partiell erf\u00fcllt",
      "10011": "Fehler der Anforderung Verarbeitung ",
      "10012": "Anforderung abgelehnt nach Zeitablaufs ",
      "10013": "Ung\u00fcltige Anforderung",
      "10014": "Ung\u00fcltiges Volumen in der Anforderung ",
      "10015": "Ung\u00fcltiger Preis in der Anforderung ",
      "10016": "Ung\u00fcltige Stops in der Anforderung ",
      "10017": "Handel ist verboten",
      "10018": "Markt ist geschlossen ",
      "10019": "Nicht genug Geld, um Anforderung zu erf\u00fcllen ",
      "10020": "Preise haben sich ver\u00e4ndert ",
      "10021": "Es gibt keine Quotationen f\u00fcr die Verarbeitung der Anforderung ",
      "10022": "Ung\u00fcltiges Datum des Orderablaufs in der Anforderung ",
      "10023": "Order Status hat sich ver\u00e4ndert ",
      "10024": "Sehr offene Anforderungen",
      "10025": "Keine Ver\u00e4nderungen in der Anforderung ",
      "10026": "Autotrading ist vom Server untersagt ",
      "10027": "Autotrading ist vom Client-Terminal untersagt ",
      "10028": "Anforderung ist f\u00fcr Verarbeitung blockiert ",
      "10029": "Order oder Position sind eingefroren ",
      "10030": "Nicht unterst\u00fctzter Durchf\u00fchrungstyp der Order nach dem Rest ",
      "10031": "keine Verbindung mit dem Handelsserver ",
      "10032": "Operation ist nur f\u00fcr reelle Kontos erlaubt",
      "10033": "Limit f\u00fcr Anzahl der Warteordern ist erreicht ",
      "10034": "Limit f\u00fcr Volumen der Ordern und Positionen f\u00fcr dieses Symbol ist erreicht ",
      "10035": "Ung\u00fcltiger oder verbotener Ordertyp",
      "10036": "Die Position mit dem angegebenen POSITION_IDENTIFIER wurde bereits geschlossen",
      "10038": "Das zu schlie\u00dfende Volumen \u00fcbersteigt das aktuelle Volumen der Position",
      "10039": "F\u00fcr die angegebene Position ist bereits eine Verkaufsorder vorhanden. Kann im Hedging Modus auftreten:beim Versuch, eine Position zur Gegenposition zu schlie\u00dfen, wenn es bereits Orders zum Schlie\u00dfen dieser Position gibt beim Versuch, eine Position ganz oder teilweise zu schlie\u00dfen, wenn das Gesamtvolumen der vorhandenen Verkaufsorders und der zu platzierenden Order das aktuelle Volumen der Position \u00fcbersteigt",
      "10040": "Die Anzahl offener Positionen, die man zur gleichen Zeit auf einem Konto haben kann, kann durch die Einstellungen des Servers beschr\u00e4nkt werden. Wenn ein Limit erreicht ist, gibt der Server beim Versuch, eine Order zu platzieren, den Fehler TRADE_RETCODE_LIMIT_POSITIONS zur\u00fcck. Die Beschr\u00e4nkung funktioniert je nach dem Modus der Verrechnung von Positionen auf dem Konto:Netting-Modus \u2014 die Anzahl offener Positionen wird ber\u00fccksichtigt. Wenn ein Limit erreicht ist, l\u00e4sst die Plattform keine weiteren Orders platzieren, deren Ausf\u00fchrung die Erh\u00f6hung der Anzahl offener Positionen verursachen kann. In Wirklichkeit l\u00e4sst die Plattform Orders nur f\u00fcr die Symbole platzieren, f\u00fcr welche es offene Positionen bereits gibt. Im Netting-Modus werden aktuelle Pending Orders nicht ber\u00fccksichtigt, denn die Ausf\u00fchrung einer Pending Order kann zur \u00c4nderung aktueller Positionen und nicht zur Erh\u00f6hung ihrer Anzahl f\u00fchren.Hedging-Modus \u2014 Pending Orders werden zusammen mit offenen Positionen ber\u00fccksichtigt, denn die Ausl\u00f6sung einer Pending Order f\u00fchrt immer zur Er\u00f6ffnung einer neuen Position. Wenn ein Limit erreicht ist, l\u00e4sst die Plattform keine Marktorders f\u00fcr Er\u00f6ffnung von Positionen sowie keine Pending Orders platzieren.",
      "10041": "Die Anfrage auf die Aktivierung der Pending Order wurde abgelehnt, die Order wurde abgebrochen",
      "10042": "Die Anfrage wurde abgelehnt, weil f\u00fcr das Symbol die Regel \"Nur Long-Positionen erlaubt\" (POSITION_TYPE_BUY) festgelegt wurde",
      "10043": "Die Anfrage wurde abgelehnt, weil f\u00fcr das Symbol die Regel \"Nur Short-Positionen erlaubt\" (POSITION_TYPE_SELL) festgelegt wurde",
      "10044": "Die Anfrage wurde abgelehnt, weil f\u00fcr das Symbol die Regel \"Nur das Schlie\u00dfen vorhandener Postionen erlaubt\" festgelegt wurde",
      "10045": "Der Auftrag wurde zur\u00fcckgewiesen, weil das Flag \"Positionsschlie\u00dfung nur nach FIFO-Regel erlaubt\" f\u00fcr das Handelskonto gesetzt ist (ACCOUNT_FIFO_CLOSE=true)",
      "10046": "Die Anfrage wurde abgelehnt, weil f\u00fcr das Handelskonto die Regel festgelegt wurde \"Gegens\u00e4tzliche Positionen ein und desselben Symbols ist deaktiviert\". Wenn das Konto z.B. eine Kaufposition hat, kann ein Nutzer keine Verkaufsposition er\u00f6ffnen oder einen schwebenden Verkaufsauftrag platzieren. Die Regel wird nur auf Konten mit Hedging-Buchhaltungssystem angewendet (ACCOUNT_MARGIN_MODE=ACCOUNT_MARGIN_MODE_RETAIL_HEDGING)."
}
