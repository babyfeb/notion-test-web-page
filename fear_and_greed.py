import requests
from bs4 import BeautifulSoup
import os

def generate_html():
    """CNN Fear and Greed Index와 TradingView 주식 차트를 포함한 HTML 파일을 생성합니다."""
    url = "https://edition.cnn.com/markets/fear-and-greed"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # --- 데이터 추출 ---
        now_indicator_elem = soup.select_one('.market-fng-gauge__dial-number-value')
        now_status_elem = soup.select_one('.market-fng-gauge__dial-label')

        if not now_indicator_elem or not now_status_elem:
            now_indicator = "N/A"
            now_status = "데이터 로딩 실패"
            indicators_data = []
        else:
            now_indicator = now_indicator_elem.text.strip()
            now_status = now_status_elem.text.strip()
            indicators_data = []
            indicators = soup.select('.market-fng-indicator__details')
            for indicator in indicators:
                title = indicator.select_one('.market-fng-indicator__title-text').text.strip()
                status = indicator.select_one('.market-fng-indicator__text').text.strip()
                indicators_data.append({'title': title, 'status': status})


        # --- HTML 생성 ---
        html_content = f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Fear & Greed Index and Stock Charts</title>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; padding: 20px; background-color: #f7f7f7; }}
                .container {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }}
                h1, h2 {{ text-align: center; color: #333; border-bottom: 1px solid #eee; padding-bottom: 10px; margin-bottom: 20px; }}
                .main-index {{ text-align: center; margin-bottom: 25px; }}
                .main-index .value {{ font-size: 3em; font-weight: bold; color: #d9534f; }}
                .main-index .status {{ font-size: 1.2em; color: #555; }}
                .indicators-list {{ list-style: none; padding: 0; }}
                .indicators-list li {{ background: #fafafa; padding: 10px; border-radius: 4px; margin-bottom: 8px; display: flex; justify-content: space-between; }}
                .indicators-list .title {{ font-weight: bold; color: #444; }}
                .indicators-list .status {{ color: #666; }}
                .charts-container {{ margin-top: 30px; }}
                .tradingview-widget-container {{ margin-bottom: 20px; height: 350px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📈 금융 대시보드</h1>
                
                <div class="fng-container">
                    <h2>CNN 공포와 탐욕 지수</h2>
                    <div class="main-index">
                        <div class="value">{now_indicator}</div>
                        <div class="status">{now_status}</div>
                    </div>
                    <ul class="indicators-list">
        """

        for item in indicators_data:
            html_content += f"""
                    <li>
                        <span class="title">{item['title']}</span>
                        <span class="status">{item['status']}</span>
                    </li>
            """

        html_content += """
                    </ul>
                </div>

                <div class="charts-container">
                    <h2>주요 종목 실시간 차트</h2>
                    
                    <div class="tradingview-widget-container">
                      <div class="tradingview-widget-container__widget"></div>
                      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
                      {{
                        "symbols": [["NASDAQ:QQQ|1D"]],
                        "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr",
                        "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false,
                        "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false,
                        "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
                        "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent",
                        "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9,
                        "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0,
                        "dateRanges": ["1d", "1m", "3m", "1y", "all"]
                      }}
                      </script>
                    </div>
                    <div class="tradingview-widget-container">
                      <div class="tradingview-widget-container__widget"></div>
                      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
                      {{
                        "symbols": [["NASDAQ:IQQQ|1D"]],
                        "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr",
                        "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false,
                        "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false,
                        "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
                        "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent",
                        "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9,
                        "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0,
                        "dateRanges": ["1d", "1m", "3m", "1y", "all"]
                      }}
                      </script>
                    </div>
                    <div class="tradingview-widget-container">
                      <div class="tradingview-widget-container__widget"></div>
                      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
                      {{
                        "symbols": [["NASDAQ:QQQI|1D"]],
                        "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr",
                        "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false,
                        "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false,
                        "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
                        "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent",
                        "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9,
                        "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0,
                        "dateRanges": ["1d", "1m", "3m", "1y", "all"]
                      }}
                      </script>
                    </div>
                    </div>
            </div>
        </body>
        </html>
        """
        return html_content

    except Exception as e:
        return f"<html><body><h1>오류 발생</h1><p>{e}</p></body></html>"

if __name__ == "__main__":
    html_output = generate_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    print("index.html 파일 생성 완료.")
