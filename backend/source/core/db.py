import pymysql
import sys
import open_dart
import sqlalchemy
import pandas as pd
from tqdm import tqdm
from time import perf_counter
import json

sys.path.append("../../")
from static import SQL

host = "localhost"
user = "root"
password = "password"
port = 3306
db_name = "finance"  ## TODO: rename into korean_fs

pymysql_connect = pymysql.connect(host=host, port=port, db=db_name, user=user, password=password, autocommit=True)

db_engine = sqlalchemy.create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db_name}")
alchemy_connect = db_engine.connect()


def get_table_data(table_name: str) -> None:

    sql = f"SELECT * FROM {table_name}"
    return pd.read_sql(sql, pymysql_connect)


def get_company_info(table_name="company_info") -> pd.DataFrame:

    sql = f"SELECT * FROM {table_name}"
    return pd.read_sql(sql, pymysql_connect)


def get_corp_codes():
    df = get_company_info()
    return df["corp_code"].tolist()


def create_table(table_name: str, schema: str) -> None:
    """Create SQL TABLE"""

    # TODO: try except handling
    with pymysql_connect.cursor() as cursor:
        sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} ({schema})
        """
        cursor.execute(sql)
    pymysql_connect.commit()


def delete_table(table_name: str) -> bool:
    """Delete SQL TABLE"""
    with pymysql_connect.cursor() as cursor:
        sql = f"""
        DROP TABLE {table_name}
        """
        cursor.execute(sql)
    pymysql_connect.commit()


def update_company_info_table(table_name: str = "company_info") -> None:
    corp_df = open_dart.getCorpCode()
    corp_df.columns = ["corp_code", "name", "stock_code", "last_update"]

    # insert df to db
    ## TODO: refactoring to update not exist corporation entry
    corp_df.to_sql(name=table_name, con=alchemy_connect, if_exists="append", index=False)


def get_company_info(table_name="company_info") -> pd.DataFrame:

    sql = f"SELECT * FROM {table_name}"
    return pd.read_sql(sql, pymysql_connect)


# Finance Statement
def get_fs(corp_code: str, bsns_year: str, table_name: str) -> pd.DataFrame:
    sql = f"""
    SELECT *  
    FROM {table_name} 
    WHERE corp_code = '{corp_code}' AND bsns_year = '{bsns_year}'
    """
    return pd.read_sql(sql, pymysql_connect)


def update_fs(corp_code: str, bsns_year: str, table_name: str, report_code: str, fs_div: str) -> bool:

    report = {
        "corp_code": corp_code,
        "bsns_year": bsns_year,
        "table_name": table_name,
        "report_code": report_code,
        "fs_div": fs_div,
        "status": "fail",  # 0: fail, 1: success, -1: error, 2:exist
        "log": "",
    }

    df = get_fs(corp_code, bsns_year, table_name)

    if not df.empty:
        print("data already exist, skip!")
        report["status"] = "exist"
        return report

    try:
        df = open_dart.get_fs_all(corp_code, bsns_year, report_code, fs_div)

    except Exception as e:
        report["status"] = "exception"
        report["log"] = str(e)
        return report

    if df is not None:
        df = df.fillna(-1).replace("", -1)
        df.to_sql(name=table_name, con=alchemy_connect, if_exists="append", index=False)
        report["status"] = "success"

    return report


def get_fs_report(corp_code, table_name="korean_fs") -> bool:
    sql = f"""
    SELECT *  
    FROM {table_name} 
    WHERE corp_code = '{corp_code}' 
    """

    return pd.read_sql(sql, pymysql_connect)


def update_fs_all(bsns_year, table, report_code, fs_div, f_path="./update_fs_all.json"):
    reports = []
    corp_codes: list = get_corp_codes()
    ts1 = perf_counter()
    for corp_code in tqdm(corp_codes):
        report = update_fs(corp_code, bsns_year, table, report_code, fs_div)
        reports.append(report)
    runtime = perf_counter() - ts1
    print(f"total runtime: {runtime:.2f} sec")

    with open(f_path, "w") as f:
        json.dump(reports, f)

    return reports


if __name__ == "__main__":

    # create_table("company_info", SQL.COMPANY_INFO_TABLE)
    # update_company_info_table()
    corp_code = "00126380"  # 삼성전자: "00126380", "LG전자": "00401731"
    bsns_year = "2022"
    report_code = "11011"  # ["11011", "11012", "11013", "11014"]
    fs_div = "CFS"  # ["CFS", "OFS"]
    code2quart = {"11011": "Q4", "11012": "Q2", "11013": "Q1", "11014": "Q3"}

    table = f"kor_fs_{fs_div}_{code2quart[report_code]}"
    print(table)
    # delete_table(table)
    create_table(table, SQL.KOREAN_FS_TABLE)
    update_fs(corp_code, bsns_year, table, report_code, fs_div)
    df = get_fs(corp_code, bsns_year, table)
    print(df)
    # # Initialize table
    # queue = [(report_code, fs_div) for report_code in report_codes for fs_div in fs_divs]

    # for report_code, fs_div in queue:
    #     df = open_dart.get_fs_all(corp_code, bsns_year, report_code, fs_div)
    #     df.to_csv(f"{table}.csv")

    # # data request
    # for report_code, fs_div in queue:
    #     table = f"kor_fs_{fs_div}_{code2quart[report_code]}"
    #     update_fs(corp_code, bsns_year, table, report_code, fs_div)
    # df = get_table_data("korean_fs")
    # print(df)
    # df = get_fs_report("00126380")
    # print(df)
