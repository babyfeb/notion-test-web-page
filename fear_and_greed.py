<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fear & Greed Index and Stock Charts</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; padding: 20px; background-color: #f7f7f7; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }
        h1, h2 { text-align: center; color: #333; border-bottom: 1px solid #eee; padding-bottom: 10px; margin-bottom: 20px; }
        .main-index { text-align: center; margin-bottom: 25px; }
        .main-index .value { font-size: 3em; font-weight: bold; color: #d9534f; }
        .main-index .status { font-size: 1.2em; color: #555; }
        .indicators-list { list-style: none; padding: 0; }
        .indicators-list li { background: #fafafa; padding: 10px; border-radius: 4px; margin-bottom: 8px; display: flex; justify-content: space-between; }
        .indicators-list .title { font-weight: bold; color: #444; }
        .indicators-list .status { color: #666; }
        .charts-container { margin-top: 30px; }
        .tradingview-widget-container { margin-bottom: 20px; height: 350px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📈 금융 대시보드</h1>
        
        <div class="fng-container">
            <h2>CNN 공포와 탐욕 지수</h2>
            <div class="main-index">
                <div class="value">58</div>
                <div class="status">Greed</div>
            </div>
            <ul class="indicators-list">
                <li><span class="title">Junk Bond Demand</span><span class="status">Greed</span></li>
                <li><span class="title">Market Momentum</span><span class="status">Extreme Greed</span></li>
                <li><span class="title">Market Volatility</span><span class="status">Neutral</span></li>
                <li><span class="title">Put and Call Options</span><span class="status">Extreme Fear</span></li>
                <li><span class="title">Safe Haven Demand</span><span class="status">Extreme Fear</span></li>
                <li><span class="title">Stock Price Breadth</span><span class="status">Greed</span></li>
                <li><span class="title">Stock Price Strength</span><span class="status">Greed</span></li>
            </ul>
        </div>

        <div class="charts-container">
            <h2>주요 종목 실시간 차트</h2>
            
            <div class="tradingview-widget-container">
              <div class="tradingview-widget-container__widget"></div>
              <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
              { "symbols": [["NASDAQ:QQQ|1D"]], "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr", "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false, "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false, "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif", "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent", "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9, "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0, "dateRanges": ["1d", "1m", "3m", "1y", "all"] }
              </script>
            </div>
            <div class="tradingview-widget-container">
              <div class="tradingview-widget-container__widget"></div>
              <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
              { "symbols": [["NASDAQ:IQQQ|1D"]], "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr", "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false, "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false, "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif", "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent", "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9, "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0, "dateRanges": ["1d", "1m", "3m", "1y", "all"] }
              </script>
            </div>
            <div class="tradingview-widget-container">
              <div class="tradingview-widget-container__widget"></div>
              <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
              { "symbols": [["NASDAQ:QQQI|1D"]], "chartOnly": false, "width": "100%", "height": "100%", "locale": "kr", "colorTheme": "light", "autosize": true, "showVolume": false, "showMA": false, "hideDateRanges": false, "hideMarketStatus": false, "hideSymbolLogo": false, "scalePosition": "right", "scaleMode": "Normal", "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif", "fontSize": "10", "noTimeScale": false, "valuesTracking": "1", "changeMode": "price-and-percent", "chartType": "area", "maLineColor": "#2962FF", "maLineWidth": 1, "maLength": 9, "backgroundColor": "rgba(255, 255, 255, 1)", "lineWidth": 2, "lineType": 0, "dateRanges": ["1d", "1m", "3m", "1y", "all"] }
              </script>
            </div>
            </div>
    </div>
</body>
</html>
