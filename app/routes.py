from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models import Stock
import requests
import json

API_KEY = 'D4FCE58NXQG93353'

def init_app(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/search', methods=['POST'])
    def search():
        symbol = request.form['symbol']
        stock = Stock.query.filter_by(symbol=symbol).first()
        if not stock:
            api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}'
            response = requests.get(api_url)
            data = response.json()
            if "Error Message" in data:
                flash("Stock symbol not found", "error")
                return redirect(url_for('index'))
            stock = Stock(symbol=symbol, data=json.dumps(data))
            db.session.add(stock)
            db.session.commit()
            flash("Stock added successfully", "success")
        return redirect(url_for('stock', symbol=stock.symbol))

    @app.route('/stock/<symbol>')
    def stock(symbol):
        stock = Stock.query.filter_by(symbol=symbol).first_or_404()
        data = json.loads(stock.data)
        return render_template('stock.html', stock=stock, data=data)

    @app.route('/stock/<symbol>/history')
    def stock_history(symbol):
        stock = Stock.query.filter_by(symbol=symbol).first_or_404()
        data = json.loads(stock.data)['Time Series (1min)']
        history = []
        for date, values in data.items():
            history.append({
                'date': date,
                'open': values['1. open'],
                'high': values['2. high'],
                'low': values['3. low'],
                'close': values['4. close'],
                'volume': values['5. volume']
            })
        return render_template('history.html', stock=stock, history=history)
