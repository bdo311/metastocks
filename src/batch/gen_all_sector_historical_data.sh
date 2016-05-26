cd ..

START_DATE="1-1-2000"


TICKER_SYMBOL_LIST1="../data/ticker-lists/1-basic-materials-ticker-list.txt"
OUTPUT_FOLDER1="../data/historical-data/1-basic-materials"
python historicalStockScraper.py $TICKER_SYMBOL_LIST1 $OUTPUT_FOLDER1 $START_DATE &

TICKER_SYMBOL_LIST2="../data/ticker-lists/2-conglomerates-ticker-list.txt"
OUTPUT_FOLDER2="../data/historical-data/2-conglomerates"
python historicalStockScraper.py $TICKER_SYMBOL_LIST2 $OUTPUT_FOLDER2 $START_DATE &

TICKER_SYMBOL_LIST3="../data/ticker-lists/3-consumer-goods-ticker-list.txt"
OUTPUT_FOLDER3="../data/historical-data/3-consumer-goods"
python historicalStockScraper.py $TICKER_SYMBOL_LIST3 $OUTPUT_FOLDER3 $START_DATE &

TICKER_SYMBOL_LIST4="../data/ticker-lists/4-financials-ticker-list.txt"
OUTPUT_FOLDER4="../data/historical-data/4-financials"
python historicalStockScraper.py $TICKER_SYMBOL_LIST4 $OUTPUT_FOLDER4 $START_DATE &

TICKER_SYMBOL_LIST5="../data/ticker-lists/5-healthcare-ticker-list.txt"
OUTPUT_FOLDER5="../data/historical-data/5-healthcare"
python historicalStockScraper.py $TICKER_SYMBOL_LIST5 $OUTPUT_FOLDER5 $START_DATE &

TICKER_SYMBOL_LIST6="../data/ticker-lists/6-industrial-goods-ticker-list.txt"
OUTPUT_FOLDER6="../data/historical-data/6-industrial-goods"
python historicalStockScraper.py $TICKER_SYMBOL_LIST6 $OUTPUT_FOLDER6 $START_DATE &

TICKER_SYMBOL_LIST7="../data/ticker-lists/7-services-ticker-list.txt"
OUTPUT_FOLDER7="../data/historical-data/7-services"
python historicalStockScraper.py $TICKER_SYMBOL_LIST7 $OUTPUT_FOLDER7 $START_DATE &

TICKER_SYMBOL_LIST8="../data/ticker-lists/8-technology-ticker-list.txt"
OUTPUT_FOLDER8="../data/historical-data/8-technology"
python historicalStockScraper.py $TICKER_SYMBOL_LIST8 $OUTPUT_FOLDER8 $START_DATE &

TICKER_SYMBOL_LIST9="../data/ticker-lists/9-utilities-ticker-list.txt"
OUTPUT_FOLDER9="../data/historical-data/9-utilities"
python historicalStockScraper.py $TICKER_SYMBOL_LIST9 $OUTPUT_FOLDER9 $START_DATE &



