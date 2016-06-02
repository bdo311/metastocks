# with_market_cap_metagenes.sh

cd /scratch/PI/rondror/akma327/MetaStocks/metastocks/src

python metagene.py ../data/historical-data/1-basic-materials/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/1-basic-materials-with-cap-metagene.txt 20080101 20151231 20090101 


python metagene.py ../data/historical-data/2-conglomerates/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/2-conglomerates-with-cap-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/3-consumer-goods/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/3-consumer-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/4-financials/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/4-financials-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/5-healthcare/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/5-healthcare-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/6-industrial-goods/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/6-industrial-goods-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/7-services/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/7-services-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/8-technology/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/8-technology-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/9-utilities/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/9-utilities-no-cap-goods-metagene.txt 20080101 20151231 20090101
