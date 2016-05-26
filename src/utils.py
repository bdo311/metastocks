# utils.py
from datetime import datetime

# Parse ticker list file 
def parseTickerList(TICKER_LIST):
    f = open(TICKER_LIST, 'r')
    symbols = []
    for line in f:
        if(line != "\n"):
            symbols.append(line.strip())
    return symbols


# Parse hyphen delimited date 
def parseDate(date):
	if(date == None): return datetime.today()
	date_info = date.split("-")
	month, day, year = int(date_info[0].strip()), int(date_info[1].strip()), int(date_info[2].strip())
	return datetime(year, month, day)
