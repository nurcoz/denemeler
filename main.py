
import yfinance as yf; print(yf.download("AAPL", period="1mo").tail(10))