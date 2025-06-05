import os
import requests
import yfinance as yf

ETF_LIST = ['CONY', 'TSLY', 'NVDY', 'MSTY']
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print(f"❌ 텔레그램 메시지 전송 실패: {response.status_code}")
        print(response.text)
    else:
        print("✅ 텔레그램 메시지 전송 성공")

def fetch_latest_dividend(etf_symbol):
    try:
        ticker = yf.Ticker(etf_symbol)
        divs = ticker.dividends

        if divs.empty:
            print(f"⚠️ {etf_symbol} 배당 정보 없음")
            return None

        latest_date = divs.index[-1].strftime('%Y-%m-%d')
        amount = divs.iloc[-1]
        return {
            "symbol": etf_symbol,
            "ex_date": latest_date,
            "cash_amount": f"${amount:.4f}"
        }
    except Exception as e:
        print(f"❌ {etf_symbol} 배당 정보 가져오기 실패: {e}")
        return None

def main():
    print(f"✅ TELEGRAM_TOKEN: {'있음' if TOKEN else '없음'}")
    print(f"✅ TELEGRAM_CHAT_ID: {'있음' if CHAT_ID else '없음'}")

    if not TOKEN or not CHAT_ID:
        print("❌ 환경 변수가 설정되지 않았습니다.")
        return

    for symbol in ETF_LIST:
        info = fetch_latest_dividend(symbol)
        if info:
            msg = (
                f"📢 {info['symbol']} 배당 정보\n"
                f"- 배당금: {info['cash_amount']}\n"
                f"- 배당 기준일: {info['ex_date']}"
            )
            print(f"📤 {symbol} 정보 전송 중...")
            send_telegram_message(msg)
        else:
            print(f"⚠️ {symbol} 배당 정보 없음 또는 전송 실패")

if __name__ == '__main__':
    main()
