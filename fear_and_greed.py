import requests
from bs4 import BeautifulSoup
import os

def generate_html():
    """CNN Fear and Greed Index와 TradingView 주식 차트를 포함한 HTML 파일을 생성합니다."""
    # 웹사이트 구조 변경에 대응하기 위해 데이터를 가져오는 부분을 수정했습니다.
    try:
        # CNN에서 직접 데이터를 제공하는 JSON API를 사용합니다. 이 방식이 더 안정적입니다.
        json_url = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
        response = requests.get(json_url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        data = response.json()

        # 최신 데이터 추출
        now_indicator = int(data['fear_and_greed']['score'])
        now_status = data['fear_and_greed']['rating'].capitalize() # 예: "fear" -> "Fear"

        # 7개의 개별 지표 데이터 추출
        indicators_data = []
        for item in data['fear_and_greed_components']:
            # 'previous_close'를 현재 값으로 사용
            title = item['indicator_name'].replace(" F&G Model", "") # 불필요한 텍스트 제거
            rating = item['rating'].capitalize()
            indicators_data.append({'title': title, 'status': rating})

    except Exception as e:
        print(f"Error fetching Fear & Greed data: {e}")
        now_indicator = "N/A"
        now_status = "데이터 로딩 실패"
        indicators_data = []


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

if __name__ == "__main__":
    html_output = generate_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    print("index.html 파일 생성 완료.")
