# utils.py

# Parse ticker list file 
def parseTickerList(TICKER_LIST):
    f = open(TICKER_LIST, 'r')
    symbols = []
    for line in f:
        if(line != "\n"):
            symbols.append(line.strip())
    return symbols