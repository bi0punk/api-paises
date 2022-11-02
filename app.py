from flask import Flask, render_template, jsonify
from urllib.request import urlopen
from unicodedata import normalize
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import numpy as np
import requests









app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello_world():
    table_MN = pd.read_html('https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses')
    print(f'Total tables: {len(table_MN)}')
    df = table_MN[0]
    df2 = table_MN[1]
    df3 = table_MN[2]
    df4 = table_MN[3]
    df5 = table_MN[4]
    df6 = table_MN[5]
    df7 = table_MN[6]
    df8 = table_MN[7]

    
    a = df.to_csv('paises_csv', encoding='utf-8', sep=';')
    a2 = df2.to_csv('paises2_csv', encoding='utf-8', sep=';')
    a3 = df3.to_csv('paises3_csv', encoding='utf-8', sep=';')
    a4 = df4.to_csv('paises4_csv', encoding='utf-8', sep=';')
    a5 = df5.to_csv('paises5_csv', encoding='utf-8', sep=';')
    a6 = df6.to_csv('paises6_csv', encoding='utf-8', sep=';')
    a7 = df7.to_csv('paises7_csv', encoding='utf-8', sep=';')
    a8 = df8.to_csv('paises8_csv', encoding='utf-8', sep=';')


    return '<h1>hola</h1>'




