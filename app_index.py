import os

import streamlit as st
import pandas as pd
import json
import pandas as pd
import plotly.graph_objects as go


f = open('Stock List.json', "r")
data = json.loads(f.read())
df = pd.DataFrame(data)
df.to_csv("data2.csv", index=False)
df2=df.loc[:, ["symbol","date", "open","high","low","close"]]
df2["date"] = pd.to_datetime(df2["date"])

for i, x in df2.groupby('symbol'):
    p = os.path.join(os.getcwd(), "{}.csv".format(i.lower()))
    x.to_csv(p, index=False)
df2.to_csv("Stock_list_essn.csv",index=False)
st.write("""
OHLC_NT
""")
st.sidebar.header('Input')

def get_ip():
    start_date=st.sidebar.text_input("Start Date","2021-01-04")
    end_date=st.sidebar.text_input("End Date","2021-08-24")
    symbol=st.sidebar.text_input("Stock Symbol","APPL")

    return start_date,end_date,symbol

def getting_data(start,end,sym):
    start=pd.to_datetime(start)
    end = pd.to_datetime(end)
    set_start=0
    set_end=0
    if sym.lower()=='aapl':
        dff=pd.read_csv('aapl.csv')
    elif sym.lower()=='abbv':
        dff=pd.read_csv('abbv.csv')
    elif sym.lower()=='abt':
        dff=pd.read_csv('abt.csv')
    elif sym.lower()=='acn':
        dff=pd.read_csv('acn.csv')
    elif sym.lower()=='adbe':
        dff=pd.read_csv('adbe.csv')
    elif sym.lower()=='adsk':
        dff=pd.read_csv('adsk.csv')
    elif sym.lower()=='amat':
        dff=pd.read_csv('amat.csv')
    elif sym.lower()=='amd':
        dff=pd.read_csv('amd.csv')
    elif sym.lower()=='amgn':
        dff=pd.read_csv('amgn.csv')
    elif sym.lower()=='amt':
        dff=pd.read_csv('amt.csv')
    elif sym.lower()=='amzn':
        dff=pd.read_csv('amzn.csv',)
    elif sym.lower()=='asml':
        dff=pd.read_csv('asml.csv')
    elif sym.lower()=='avgo':
        dff=pd.read_csv('avgo.csv.csv')
    elif sym.lower()=='axp':
        dff=pd.read_csv('axp.csv')
    elif sym.lower()=='ba':
        dff=pd.read_csv('ba.csv')
    elif sym.lower()=='baba':
        dff=pd.read_csv('baba.csv')
    elif sym.lower()=='bac':
        dff=pd.read_csv('bac.csv.csv')
    elif sym.lower()=='bbl':
        dff=pd.read_csv('bbl.csv')
    elif sym.lower()=='bhp':
        dff=pd.read_csv('bhp.csv')
    elif sym.lower()=='blk':
        dff=pd.read_csv('blk.csv')
    elif sym.lower()=='bmy':
        dff=pd.read_csv('bmy.csv')
    elif sym.lower()=='bud':
        dff=pd.read_csv('bud.csv')
    elif sym.lower()=='csco':
        dff=pd.read_csv('csco.csv')
    elif sym.lower()=='dis':
        dff=pd.read_csv('dis.csv')
    elif sym.lower()=='dhr':
        dff=pd.read_csv('dhr.csv' )
    elif sym.lower()=='fb':
        dff=pd.read_csv('fb.csv' )
    elif sym.lower()=='goog':
        dff=pd.read_csv('goog.csv' )
    elif sym.lower()=='googl':
        dff=pd.read_csv('googl.csv' )
    elif sym.lower()=='hd':
        dff=pd.read_csv('hd.csv' )
    elif sym.lower()=='ibm':
        dff=pd.read_csv('ibm.csv' )
    elif sym.lower()=='xom':
        dff=pd.read_csv('xom.csv' )
    elif sym.lower()=='tsla':
        dff=pd.read_csv('tsla.csv' )
    elif sym.lower()=='snap':
        dff=pd.read_csv('snap.csv')
    elif sym.lower()=='sny':
        dff=pd.read_csv('sny.csv')
    elif sym.lower()=='sony':
        dff=pd.read_csv('sony.csv')
    elif sym.lower()=='nflx':
        dff=pd.read_csv('nflx.csv')
    elif sym.lower()=='orcl':
        dff=pd.read_csv('orcl.csv')
    else:
        dff=pd.DataFrame(columns=['symbol','date','open','high','low','close'])


    for row in range(0,len(dff)):

        if start<=pd.to_datetime(dff['date'][row]):
            set_start=row
            print(row)
            break
    for row1 in range(0,len(dff)):
        if end>=pd.to_datetime(dff['date'][len(dff)-1-row1]):
            set_end=len(dff)-1-row1
            print(set_end)
            break
    dff.set_index(pd.DatetimeIndex(dff['date'].values))
    return dff.iloc[set_start:set_end+1,:]


start,end,sym=get_ip()
dfx=getting_data(start,end,sym)

st.header("Chart\n")


fig = go.Figure(data=[go.Ohlc(x=dfx['date'],open=dfx['open'],high=dfx['high'],low=dfx['low'], close=dfx['close'])])

st.plotly_chart(fig)

