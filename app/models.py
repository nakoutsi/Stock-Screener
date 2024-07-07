from app import db

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    data = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Stock {self.symbol}>'
