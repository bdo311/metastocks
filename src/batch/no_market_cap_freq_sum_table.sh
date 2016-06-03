# no_market_cap_freq_sum_table.sh

# no_market_cap_metagenes.sh

cd /scratch/PI/rondror/akma327/MetaStocks/metastocks/src

python metagene.py ../data/historical-data/1-basic-materials/ none ../data/stock_freq_summary_table/no-market-cap/1-basic-materials-no-cap-metagene.txt 20040101 20151231 20090306 -summary &


python metagene.py ../data/historical-data/2-conglomerates/ none ../data/stock_freq_summary_table/no-market-cap/2-conglomerates-no-cap-metagene.txt 20040101 20151231 20090306 -summary &


python metagene.py ../data/historical-data/3-consumer-goods/ none ../data/stock_freq_summary_table/no-market-cap/3-consumer-no-cap-goods-metagene.txt 20040101 20151231 20090306 -summary &


python metagene.py ../data/historical-data/4-financials/ none ../data/stock_freq_summary_table/no-market-cap/4-financials-no-cap-goods-metagene.txt 20040101 20151231 20090306 -summary &


python metagene.py ../data/historical-data/5-healthcare/ none ../data/stock_freq_summary_table/no-market-cap/5-healthcare-no-cap-goods-metagene.txt 20040101 20151231 20090306 -summary &


python metagene.py ../data/historical-data/6-industrial-goods/ none ../data/stock_freq_summary_table/no-market-cap/6-industrial-goods-no-cap-goods-metagene.txt 20040101 20151231 20090306 -summary &


python metagene.py ../data/historical-data/7-services/ none ../data/stock_freq_summary_table/no-market-cap/7-services-no-cap-goods-metagene.txt 20040101 20151231 20090306 -summary &


python metagene.py ../data/historical-data/8-technology/ none ../data/stock_freq_summary_table/no-market-cap/8-technology-no-cap-goods-metagene.txt 20040101 20151231 20090306 -summary &


python metagene.py ../data/historical-data/9-utilities/ none ../data/stock_freq_summary_table/no-market-cap/9-utilities-no-cap-goods-metagene.txt 20040101 20151231 20090306 -summary &

