## Introduction
You should be able to run the script after installing the following required package using pip, you can do so using  
```
pip install --user requests
```
I am using python3, but the exact same code should work for python2 as well  

## How to use it
If you run:
```
python stock.py
```
Then then three csv files will be created. Those files contain data for S&P 500, Dow Jones, and NASDAQ indicators.  
You can also run the script explicitly specifying the stock you want to look at by providing the stock SYMBOL:  
```
python stock.py GOOG #for google
python stock.py AAPL #for apple
```