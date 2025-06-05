import os
import requests
from bs4 import BeautifulSoup

ETF_LIST = ['cony', 'tsly', 'nvdy', 'msty']
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    
    if response.status_code != 200:
        print(f"❌ 텔레그램 메시지 전송 실패: {response.status_code}")
        print(f"응답 내용: {response.text}")
    else:
        print("✅ 텔레그램 메시지 전송 성공")

def fetch_dividend_info(etf_symbol):
    url = f"https://www.nasdaq.com/market-activity/funds-and-etfs/{etf_symbol}/dividend-history"
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tbody tr')
        if not rows:
            print(f"⚠️ {etf_symbol.upper()} 배당 정보 없음 (table 행 없음)")
            return None
        tds = [td.text.strip() for td in rows[0].find_all('td')]
        if len(tds) < 3:
            print(f"⚠️ {etf_symbol.upper()} 배당 정보 부족 (td 개수 {len(tds)})")
            return None
        return {
            "symbol": etf_symbol.upper(),
            "ex_date": tds[0],
            "cash_amount": tds[1],
            "pay_date": tds[2]
        }
    except Exception as e:
        print(f"❌ {etf_symbol.upper()} 배당 정보 크롤링 중 오류: {e}")
        return None

def main():
    print(f"✅ TELEGRAM_TOKEN: {'있음' if TOKEN else '없음'}")
    print(f"✅ TELEGRAM_CHAT_ID: {'있음' if CHAT_ID else '없음'}")

    if not TOKEN or not CHAT_ID:
        print("❌ 환경 변수(TOKEN 또는 CHAT_ID)가 설정되지 않았습니다.")
        return

    for symbol in ETF_LIST:
        info = fetch_dividend_info(symbol)
        if info:
            msg = (
                f"📢 {info['symbol']} 배당 정보\n"
                f"- 배당금: {info['cash_amount']}\n"
                f"- 배당락일: {info['ex_date']}\n"
                f"- 지급일: {info['pay_date']}"
            )
            print(f"📤 {info['symbol']} 정보 전송 중...")
            send_telegram_message(msg)
        else:
            print(f"⚠️ {symbol.upper()}의 배당 정보를 전송하지 않음 (정보 없음)")

if __name__ == '__main__':
    try:
        main()
        print("✅ 스크립트 실행 완료")
    except Exception as e:
        print(f"❌ 전체 실행 중 오류 발생: {e}")
