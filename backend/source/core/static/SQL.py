COMPANY_INFO_TABLE = """
corp_code VARCHAR(20),
corp_name VARCHAR(40),
stock_code VARCHAR(20),
sector VARCHAR(100),
product VARCHAR(100),
market VARCHAR(1),
modify_date DATE,
PRIMARY KEY (corp_code)
"""

STOCK_DATA_TABLE = """
reprt_no BIGINT,
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


STOCK_DATA_TABLE = """
name VARCHAR(8),
asset BIGINT,
income BIGINT,
profit BIGINT,
revenue BIGINT,
liability BIGINT


"""


QUERY_STOCK_DATA = """
WITH T1 AS (
    SELECT
        corp_code,
        MAX(
            CASE
                WHEN account_id = 'ifrs-full_Assets' THEN thstrm_amount
            END
        ) AS 'asset',
        MAX(
            CASE
                WHEN account_id = 'dart_OperatingIncomeLoss' THEN thstrm_amount
            END
        ) AS 'income',
        MAX(
            CASE
                WHEN account_id = 'ifrs-full_ProfitLoss' THEN thstrm_amount
            END
        ) AS 'profit',
        MAX(
            CASE
                WHEN account_id = 'ifrs-full_Revenue' THEN thstrm_amount
            END
        ) AS 'revenue',
        MAX(
            CASE
                WHEN account_id = 'ifrs-full_Liabilities' THEN thstrm_amount
            END
        ) AS 'liability'
    FROM
        `kor_fs_CFS_Q4`
    WHERE
        bsns_year = 2022
    GROUP BY
        corp_code
)
SELECT
    corp_name AS name,
    asset,
    income,
    profit,
    revenue,
    liability,
    market
FROM
    T1
    LEFT JOIN company_info AS T2 ON T1.corp_code = T2.corp_code
"""
