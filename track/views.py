from django.shortcuts import render, redirect
import uuid
from django.http import HttpResponse
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf
# Create your views here.

def index(request):
    txt=request.GET.get('search_inp')
    data = yf.download(tickers='UBER', period='1Wk', interval='1m')
    chng=data['Adj Close'].at_time('2022-05-27 16:00:00-04:00')[0]-data['Adj Close'].at_time('2022-05-26 16:00:00-04:00')[0]
    return render(request,'index.html',{'txt':txt,'open':data['Open'][0],'High':data['High'][0],'Low':data['Low'][0],'Close':data['Close'][0],'ltp':data['Adj Close'][0],'chng':chng})

# def sym(request):
#     txt=request.GET.get('search_inp')
#     print(txt)
#     return HttpResponse(txt) 
