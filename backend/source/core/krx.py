from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_market_info() -> pd.DataFrame:
    """Get stock market information"""

    corp_cls_to_market = {
        "Y": "stockMkt",
        "K": "kosdaqMkt",
        "N": "konexMkt",
    }

    stock_market_dict = {
        "stock_code": [],
        "corp_name": [],
        "sector": [],
        "product": [],
        "market": [],
    }

    for corp_cls in corp_cls_to_market.keys():

        market_type = corp_cls_to_market[corp_cls]
        url = "https://kind.krx.co.kr/corpgeneral/corpList.do"
        headers = {"Referer": "https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage"}
        params = {
            "method": "download",
            "pageIndex": 1,
            "currentPageSize": 5000,
            "orderMode": 3,
            "orderStat": "D",
            "searchType": 13,
            "marketType": market_type,
            "fiscalYearEnd": "all",
            "location": "all",
        }

        resp = requests.post(url=url, params=params, headers=headers)
        resp.text
        html = BeautifulSoup(resp.text, "html.parser")
        rows = html.find_all("tr")

        for row in rows[:]:
            cols = row.find_all("td")
            if len(cols) > 0:
                corp_name = cols[0].text.strip()
                stock_code = cols[1].text.strip()
                sector = cols[2].text.strip()
                product = cols[3].text.strip()

                stock_market_dict["stock_code"].append(stock_code.rjust(6, "0"))
                stock_market_dict["corp_name"].append(corp_name)
                stock_market_dict["sector"].append(sector)
                stock_market_dict["product"].append(product)
                stock_market_dict["market"].append(corp_cls)

                assert (
                    len(stock_market_dict["stock_code"])
                    == len(stock_market_dict["corp_name"])
                    == len(stock_market_dict["sector"])
                    == len(stock_market_dict["product"])
                    == len(stock_market_dict["market"])
                )

    return pd.DataFrame(stock_market_dict)
