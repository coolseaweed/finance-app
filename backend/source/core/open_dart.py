import requests
import pandas as pd
import io
import zipfile
import xml.etree.ElementTree as et
import os
from ratelimit import limits, RateLimitException, sleep_and_retry

DART_KEY = os.environ.get("DART_KEY", None)
BASE_URL = "https://opendart.fss.or.kr/api"


def get_fs(corp_code, bsns_year, report_code="11011"):
    """DART API로 부터 재무제표 불러오는 함수"""
    URL = "https://opendart.fss.or.kr/api/"
    URL += "fnlttMultiAcnt.json" if "," in corp_code else "fnlttSinglAcnt.json"

    params = {
        "crtfc_key": DART_KEY,
        "corp_code": corp_code,
        "bsns_year": bsns_year,  # 사업년도
        "reprt_code": report_code,  # "11011": 사업보고서
    }

    res = requests.get(URL, params=params, verify=False).json()

    if "list" not in res:
        return None
    return pd.DataFrame(res["list"])


@sleep_and_retry
@limits(calls=60, period=100)
def get_fs_all(corp_code: str, bsns_year: str, report_code: str = "11011", fs_div: str = "CFS") -> pd.DataFrame:
    """DART API로 부터 전체 재무제표 불러오는 함수
    corp_code: 기업코드
    report_code:
        - "11011": 사업보고서
        - "11012": 반기보고서
        - "11013": 1분기보고서
        - "11014": 3분기보고서
    fs_div:
        - CFS: 연결재무제표
        - OFS: 개별재무제표
    """
    URL = f"{BASE_URL}/fnlttSinglAcntAll.json"
    params = {
        "crtfc_key": DART_KEY,
        "corp_code": corp_code,
        "bsns_year": bsns_year,
        "reprt_code": report_code,
        "fs_div": fs_div,
    }

    res = requests.get(URL, params=params).json()

    if "list" not in res:
        return None
    return pd.DataFrame(res["list"])


def get_corp_codes() -> pd.DataFrame:
    """
    OpenDART 기업 고유번호 받아오기
    return value: 주식코드를 가진 업체의 DataFrame
    """
    params = {"crtfc_key": DART_KEY}

    items = ["corp_code", "corp_name", "stock_code", "modify_date"]
    url = "https://opendart.fss.or.kr/api/corpCode.xml"  # 요청 url
    res = requests.get(url, params=params, verify=False)  # url 불러오기
    zfile = zipfile.ZipFile(io.BytesIO(res.content))  # zip file 받기
    fin = zfile.open(zfile.namelist()[0])  # zip file 열고
    root = et.fromstring(fin.read().decode("utf-8"))  # utf-8 디코딩
    data = []
    for child in root:
        if len(child.find("stock_code").text.strip()) > 1:  # 종목코드가 있는 경우
            data.append([])  # data에 append하라
            for item in items:
                data[-1].append(child.find(item).text)
    df = pd.DataFrame(data, columns=items)
    return df


if __name__ == "__main__":
    # corp_code = "00126380"
    # bsn_year = "2022"
    # fs_div = "OFS"
    # fn_state = get_fs_all(corp_code, bsn_year, fs_div=fs_div)
    # fn_state.to_csv(f"{corp_code}_{bsn_year}_{fs_div}.csv")
    # print(type(fn_state))
