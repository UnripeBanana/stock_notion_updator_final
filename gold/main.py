from domestic_gold.update import 
from data.domestic_gold import get_gold_price


from domestic_stock.read import get_ticker
from domestic_stock.update import update_stock_DB
from data.domestic_stock import get_naver_prop, get_yfinance_prop

def domestic_stock_main (pages):
  for page in pages:
  
    ticker = get_ticker(page)

    if not ticker:
      continue
    
    stock_info = {
        **get_naver_prop(ticker),
        **get_yfinance_prop(ticker)
    }
  
    update_stock_DB(page, stock_info)

"""
  "price": int(gold["closePrice"].replace(",", "")),           # 현재가
  "change": int(gold["fluctuations"].replace(",", "")),        # 전일대비
  "rate": float(gold["fluctuationsRatio"]),                    # 등락률
"""
