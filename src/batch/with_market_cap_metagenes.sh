# with_market_cap_metagenes.sh

cd /scratch/PI/rondror/akma327/MetaStocks/metastocks/src

python metagene.py ../data/historical-data/1-basic-materials/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/1-basic-materials-with-cap-metagene.txt 20040101 20151231 20090306 -metagene &


python metagene.py ../data/historical-data/2-conglomerates/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/2-conglomerates-with-cap-metagene.txt 20040101 20151231 20090306 -metagene &


python metagene.py ../data/historical-data/3-consumer-goods/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/3-consumer-goods-with-cap-metagene.txt 20040101 20151231 20090306 -metagene &


python metagene.py ../data/historical-data/4-financials/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/4-financials-with-cap-metagene.txt 20040101 20151231 20090306 -metagene &


python metagene.py ../data/historical-data/5-healthcare/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/5-healthcare-with-cap-metagene.txt 20040101 20151231 20090306 -metagene &


python metagene.py ../data/historical-data/6-industrial-goods/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/6-industrial-goods-with-cap--metagene.txt 20040101 20151231 20090306 -metagene &


python metagene.py ../data/historical-data/7-services/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/7-services-with-cap-metagene.txt 20040101 20151231 20090306 -metagene &


python metagene.py ../data/historical-data/8-technology/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/8-technology-with-cap-metagene.txt 20040101 20151231 20090306 -metagene &


python metagene.py ../data/historical-data/9-utilities/ ../data/marketcaps.csv ../data/metagene_output/with-market-cap/9-utilities-with-cap-metagene.txt 20040101 20151231 20090306 -metagene &
