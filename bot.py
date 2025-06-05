import os
import requests
from bs4 import BeautifulSoup

ETF_LIST = ['cony', 'tsly', 'nvdy', 'msty']
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def fetch_dividend_info(etf_symbol):
    url = f"https://www.nasdaq.com/market-activity/funds-and-etfs/{etf_symbol}/dividend-history"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.select('table tbody tr')
    if not rows:
        return None
    tds = [td.text.strip() for td in rows[0].find_all('td')]
    if len(tds) < 3:
        return None
    return {
        "symbol": etf_symbol.upper(),
        "ex_date": tds[0],
        "cash_amount": tds[1],
        "pay_date": tds[2]
    }

def main():
    for symbol in ETF_LIST:
        info = fetch_dividend_info(symbol)
        if info:
            msg = (
                f"📢 {info['symbol']} 배당 정보\n"
                f"- 배당금: {info['cash_amount']}\n"
                f"- 배당락일: {info['ex_date']}\n"
                f"- 지급일: {info['pay_date']}"
            )
            send_telegram_message(msg)

if __name__ == '__main__':
    main()
