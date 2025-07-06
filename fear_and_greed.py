import os

def generate_final_html():
    """
    데이터 요청 부분을 Python이 아닌 Javascript로 넘겨
    사용자 브라우저에서 직접 CNN API를 호출하도록 HTML 파일을 생성합니다.
    이 방식은 깃허브 서버의 IP가 차단되는 문제를 근본적으로 해결합니다.
    """

    # HTML 구조와 Javascript 코드를 포함합니다.
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
            .main-index .value {{ font-size: 3em; font-weight: bold; color: #d9534f; min-height: 60px; }}
            .main-index .status {{ font-size: 1.2em; color: #555; }}
            .indicators-list {{ list-style: none; padding: 0; min-height: 100px; }}
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
                    <div id="fng-value" class="value">...</div>
                    <div id="fng-status" class="status">Loading...</div>
                </div>
                <ul id="fng-list" class="indicators-list">
                    <li>데이터를 불러오는 중입니다...</li>
                </ul>
            </div>

            <div class="charts-container">
                <h2>주요 종목 실시간 차트</h2>
                
                <div class="tradingview-widget-container">
                  <div class="tradingview-widget-container__widget"></div>
                  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
                  {{ "symbols": [["NASDAQ:QQQ|1D"]], "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr", "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false, "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false, "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif", "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent", "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9, "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0, "dateRanges": ["1d", "1m", "3m", "1y", "all"] }}
                  </script>
                </div>
                <div class="tradingview-widget-container">
                  <div class="tradingview-widget-container__widget"></div>
                  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
                  {{ "symbols": [["NASDAQ:IQQQ|1D"]], "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr", "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false, "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false, "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif", "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent", "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9, "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0, "dateRanges": ["1d", "1m", "3m", "1y", "all"] }}
                  </script>
                </div>
                <div class="tradingview-widget-container">
                  <div class="tradingview-widget-container__widget"></div>
                  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
                  {{ "symbols": [["NASDAQ:QQQI|1D"]], "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr", "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false, "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false, "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif", "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent", "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9, "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0, "dateRanges": ["1d", "1m", "3m", "1y", "all"] }}
                  </script>
                </div>
                </div>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const FNG_API_URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata";
                
                const valueElem = document.getElementById('fng-value');
                const statusElem = document.getElementById('fng-status');
                const listElem = document.getElementById('fng-list');

                fetch(FNG_API_URL)
                    .then(response => {{
                        if (!response.ok) {{
                            throw new Error('Network response was not ok ' + response.statusText);
                        }}
                        return response.json();
                    }})
                    .then(data => {{
                        valueElem.textContent = Math.round(data.fear_and_greed.score);
                        statusElem.textContent = data.fear_and_greed.rating.charAt(0).toUpperCase() + data.fear_and_greed.rating.slice(1);
                        
                        listElem.innerHTML = ''; // Clear loading message
                        data.fear_and_greed_components.forEach(item => {{
                            const li = document.createElement('li');
                            const title = item.indicator_name.replace(" F&G Model", "");
                            const status = item.rating.charAt(0).toUpperCase() + item.rating.slice(1);
                            li.innerHTML = `<span class="title">${{title}}</span><span class="status">${{status}}</span>`;
                            listElem.appendChild(li);
                        }});
                    }})
                    .catch(error => {{
                        console.error("Failed to fetch Fear & Greed data:", error);
                        valueElem.textContent = 'N/A';
                        statusElem.textContent = '데이터 로드 실패';
                        listElem.innerHTML = '<li>오류가 발생했습니다.</li>';
                    }});
            }});
        </script>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    html_output = generate_final_html()
    with open("index.html", "w", encoding="utf-8") as f:
