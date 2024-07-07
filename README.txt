Stock Screener App
Description
The Stock Screener App is a web-based application that allows users to search for and view detailed stock data. Users can enter a stock symbol to retrieve real-time data from the Alpha Vantage API, which is then stored in a local SQLite database for quick access. The app provides an intuitive interface to display stock information and history, with the ability to load more data dynamically.

Features
Stock Search: Enter a stock symbol to retrieve and display current stock data.
Real-Time Data: Fetches real-time stock data using the Alpha Vantage API.
Database Storage: Saves stock data to a local SQLite database for efficient data retrieval.
Stock Data Display: Presents stock data in a tabular format with an option to show more rows.
Stock History: View historical data for a selected stock symbol.
User-Friendly Interface: Clean and simple UI with navigation buttons to return to search or homepage.

Technologies Used
Backend: Flask (Python)
Frontend: HTML, CSS, Bootstrap, JavaScript (jQuery)
Database: SQLite
API: Alpha Vantage API for fetching stock data

How to Run

Clone the repository:

bash
git clone https://github.com/your-username/stock-screener.git
cd stock-screener
Create a virtual environment and install dependencies:

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

Set up the database:
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Run the application:

bash
python run.py
Access the application:
Open your web browser and navigate to http://127.0.0.1:5000/.

Folder Structure
stock-screener/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── stock.html
│   │   └── history.html
├── instance/
│   └── stocks.db
├── run.py
├── requirements.txt
└── README.md

Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.