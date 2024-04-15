from sqlalchemy.types import BigInteger, Integer, String, DATE

COMPANY_INFO_TABLE = """
corp_code VARCHAR(20),
stock_code VARCHAR(20),
name VARCHAR(40),
last_update DATE,
PRIMARY KEY (corp_code)
"""


KOREAN_FS_TABLE = """
rcept_no BIGINT,
reprt_code VARCHAR(8),
bsns_year VARCHAR(8),
corp_code VARCHAR(8),
sj_div VARCHAR(4),
sj_nm VARCHAR(256),
account_id VARCHAR(256),
account_nm VARCHAR(256),
account_detail VARCHAR(256),
thstrm_nm VARCHAR(64),
thstrm_amount BIGINT,
frmtrm_nm VARCHAR(64),
frmtrm_amount BIGINT,
bfefrmtrm_nm VARCHAR(64),
bfefrmtrm_amount BIGINT,
ord INT,
currency VARCHAR(8),
thstrm_add_amount BIGINT
"""


KOREAN_FS_SCHEMA = {
    "rcept_no": BigInteger,
    "reprt_code": String(8),
    "bsns_year": String(8),
    "corp_code": String(8),
    "sj_div": String(4),
    "sj_nm": String(256),
    "account_id": String(256),
    "account_nm": String(256),
    "account_detail": String(256),
    "thstrm_nm": String(64),
    "thstrm_amount": BigInteger,
    "frmtrm_nm": String(64),
    "frmtrm_amount": BigInteger,
    "bfefrmtrm_nm": String(64),
    "bfefrmtrm_amount": BigInteger,
    "ord": Integer,
    "currency": String(8),
    "thstrm_add_amount": BigInteger,
}


TEST_1_QUERY = """
SELECT
    account_id,
    account_nm,
    thstrm_amount,
    frmtrm_amount,
    bfefrmtrm_amount,
    ord
FROM
    korean_fs
WHERE
    corp_code = '00126380'
    AND account_id IN (
        'ifrs-full_Revenue',
        "ifrs-full_CostOfSales",
        "ifrs-full_GrossProfit",
        "dart_TotalSellingGeneralAdministrativeExpenses",
        "dart_OperatingIncomeLoss",
        "dart_OtherGains",
        "dart_OtherLosses",
        "ifrs-full_FinanceIncome",
        'ifrs-full_CurrentAssets',
        'ifrs-full_Assets'
    )
ORDER BY
    ord
"""
