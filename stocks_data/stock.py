import requests
import json
from datetime import datetime
import sys
import time

stocks = ['^GSPC', '^DJI', '^IXIC']

def convert_time(timestamp):
	return datetime.fromtimestamp(timestamp)

def write_to_csv(timestamp, data, stock):
	with open(stock+'.csv', 'w') as f:
		header = ','.join(['time'] + list(data.keys()))
		indicators = list(data.keys())
		f.write(header + '\n')
		for i in range(len(timestamp)-1, -1, -1):
			line = [convert_time(timestamp[i])]
			for indicator in indicators:
				line.append(data[indicator][i])
			f.write(','.join([str(x) for x in line])+'\n')

def crawl(stock):
	url = "https://query1.finance.yahoo.com/v8/finance/chart/{}?symbol={}&period1=1362459600&period2={}&interval=1d".format(stock, stock, int(time.time()))
	response = requests.get(url)
	timestamp = json.loads(response.text)['chart']['result'][0]['timestamp']
	data = json.loads(response.text)['chart']['result'][0]['indicators']['quote'][0]
	write_to_csv(timestamp, data, stock)

if __name__=='__main__':
	if len(sys.argv)<2:
		for stock in stocks:
			crawl(stock)
	else:
		crawl(sys.argv[1])
