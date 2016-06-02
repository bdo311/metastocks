# no_market_cap_metagenes.sh

cd /scratch/PI/rondror/akma327/MetaStocks/metastocks/src

python metagene.py ../data/historical-data/1-basic-materials/ none ../data/metagene_output/no-market-cap/1-basic-materials-no-cap-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/2-conglomerates/ none ../data/metagene_output/no-market-cap/2-conglomerates-no-cap-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/3-consumer-goods/ none ../data/metagene_output/no-market-cap/3-consumer-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/4-financials/ none ../data/metagene_output/no-market-cap/4-financials-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/5-healthcare/ none ../data/metagene_output/no-market-cap/5-healthcare-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/6-industrial-goods/ none ../data/metagene_output/no-market-cap/6-industrial-goods-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/7-services/ none ../data/metagene_output/no-market-cap/7-services-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/8-technology/ none ../data/metagene_output/no-market-cap/8-technology-no-cap-goods-metagene.txt 20080101 20151231 20090101


python metagene.py ../data/historical-data/9-utilities/ none ../data/metagene_output/no-market-cap/9-utilities-no-cap-goods-metagene.txt 20080101 20151231 20090101

