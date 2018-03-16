#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 23:00:31 2018

@author: adamsonbryant
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#### make crypto index ####

#import csvs
btccsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/bitcoin_price-csv.csv", index_col=0)
ethcsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/ethereum_price-csv.csv", index_col=0)
ripplecsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/ripple_price-csv.csv", index_col=0)
btccashcsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/bitcoin_cash_price-csv.csv", index_col=0)
ltccsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/litecoin_price-csv.csv", index_col=0)
neocsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/neo_price-csv.csv", index_col=0)
monerocsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/monero_price-csv.csv", index_col=0)
dashcsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/dash_price-csv.csv", index_col=0)
nemcsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/nem_price-csv.csv", index_col=0)
iotacsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/iota_price-csv.csv", index_col=0)
datecsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/qtum_price-csv.csv")
#make list of cryptos
cryptos=[btccsv, ethcsv, ripplecsv, btccashcsv, ltccsv, neocsv, monerocsv, dashcsv, nemcsv, iotacsv]
cryptonames=["Bitcoin", "Ethereum", "Ripple", "Bitcoin Cash", "Litecoin", "NEO", "Monero", "Dash", "NEM", "IOTA"]
#add column in each for price/starting price(to get relative growth between each), store in new list
cryptosrel=[]
for coin in cryptos:
    coinnew = None
    coinnew = coin.iloc[0:182,3]
    divisor = None
    divisor = coinnew.iloc[-1]
    coinnew=coinnew.divide(divisor)
    coinnew=coinnew.to_frame()
    coinnew["Cap"]=coin.iloc[0:182, 5]
    cryptosrel.append(coinnew)
#make market cap plot
totalcap=np.zeros(182)
for coin in cryptos:
    coinmcap = coin.iloc[0:182, 5]
    cmcap = coinmcap.as_matrix(columns=None)
    ccap=np.zeros(182)
    for num in range(cmcap.shape[0]):
        ccap[num]=int(cmcap[num].replace(",",""))
    totalcap=totalcap+ccap
relativecap=totalcap/totalcap[-1]
relcapdf=pd.DataFrame(relativecap)
relcapdf["Date"]=datecsv.iloc[0:182, 0]

# add total cap to dfs
tcapseries=pd.Series(totalcap)
tcapseries=tcapseries.to_frame()
tcapseries["Date"]=datecsv.iloc[0:182, 0]
tcapseries=tcapseries.set_index("Date")
for cry in range(len(cryptosrel)):
    (cryptosrel[cry])["TCAP"]=tcapseries
# make adjusted prices
adjustedprices=[]
for cp in cryptosrel:
    pricecapadj=[]
    for index, row in cp.iterrows(): 
        capint=int(row["Cap"].replace(",",""))
        capper=capint/row["TCAP"]
        price=row[0]*capper
        pricecapadj.append(price)
    pricecapser=pd.Series(pricecapadj)
    pricecapser=pricecapser.to_frame()
    pricecapser["Date"]=datecsv.iloc[0:182, 0]
    pricecapser=pricecapser.set_index("Date")
    adjustedprices.append(pricecapser)
# create index 
indexarray=np.zeros(182)
for ap in adjustedprices:
    temp=ap.iloc[:,0]
    tempar=temp.as_matrix()
    indexarray=indexarray+tempar
indexdf= pd.DataFrame(data=indexarray, index=datecsv.iloc[0:182,0])

#### make stock indices ####

#import csvs
googcsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/usstocks/GOOG.csv", index_col=0)
appcsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/usstocks/AAPL.csv", index_col=0)
djicsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/usstocks/^DJI.csv", index_col=0)
gspccsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/usstocks/^GSPC.csv", index_col=0)
ixiccsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/usstocks/^IXIC.csv", index_col=0)
ssecsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/SSE.csv", index_col=0)
hsicsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/HSI-csv.csv", index_col=0)
relcapcsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/relcap.csv", index_col=2)
datecsv = pd.read_csv("/Users/adamsonbryant/Documents/Duke Spring 2018/Compsci216/projectdata/cryptos/relcap.csv")

#make list of stocks
usstocks=[djicsv, gspccsv, ixiccsv]
plotnames=[]
sseandhsi=[ssecsv, hsicsv]

#make relative prices
stocksrel=[]
for stk in usstocks:
    stknew = None
    stknew = stk.iloc[8:132,3]
    divisor = None
    divisor = stknew.iloc[-1]
    stknew=stknew.divide(divisor)
    stocksrel.append(stknew)
for stk in sseandhsi:
    stknew = None
    stknew = stk.iloc[1:123,0]
    divisor = None
    divisor = stknew.iloc[0]
    stknew=stknew.divide(divisor)
    stocksrel.append(stknew)
#relcap=relcapcsv.iloc[:,1]
#stocksrel.append(relcap)
    
# create dict of dates to numbers
dates=datecsv.iloc[:, 2].tolist()
nums=list(range(182))
nums.reverse()
datestonums=dict(zip(dates, nums))

# relabel dfs
for mkt in range(len(stocksrel)):
    stocksrel[mkt]=stocksrel[mkt].rename(datestonums)
# add crypto
indexdf=indexdf.rename(datestonums)
stocksrel.append(indexdf)

# make derivative graphs
stkders=[]
for x in range(len(stocksrel)):
    skder=[]
    for n in range(len(stocksrel[x])-1):
        cur=(stocksrel[x]).iloc[n]
        nxt=(stocksrel[x]).iloc[n+1]
        skder.append(cur-nxt)
    derdates=list(stocksrel[x].index)
    derdates=derdates[0:-1]
    skderdf=pd.DataFrame(data=skder, index=derdates)
    stkders.append(skderdf)

#### create the plot ####

# scale the crypto graph to see trends easier
stkders[5]=stkders[5].multiply(0.05)

#plot the indices, comment out those plot lines to change which are visible 

plt.plot(stkders[0]); plotnames.append("DOW") #DOW
plt.plot(stkders[1]); plotnames.append("S&P")  #S&P
plt.plot(stkders[2]); plotnames.append("NASDAQ")  #NASDAQ
plt.plot(stkders[3]); plotnames.append("SSE")  #SSE
plt.plot(stkders[4]); plotnames.append("HSI")  #HSI
plt.plot(stkders[5]); plotnames.append("Crypto")  #Crypto

plt.ylabel("Price in terms of price on first day")
plt.xlabel("Date")
plt.legend(plotnames)
plt.title("Slopes of Indices over Time")
plt.xticks([0,30,60,90, 120, 150, 180], ["August 22nd", "September 22nd", "October 22nd", "November 22nd", "December 22nd", "January 22nd", "February 22nd"], rotation=45)
plt.show