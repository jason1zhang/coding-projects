-- Number of searches by bad customers

DROP TABLE IF EXISTS {table_name};

CREATE TABLE {table_name}

AS
SELECT
    event_dt        AS ic_srp_trans_dt
    , event_hr      AS ic_srp_trans_hr
    , count(1)      AS ic_srp_cnt
FROM (
    SELECT
        srp.*
    FROM (
        SELECT
            SESSION_START_DT
            , GUID
            , SESSION_SKEY
            , SEQNUM
            , USER_ID
            , EVENT_TIMESTAMP
            , date(EVENT_TIMESTAMP)     AS event_dt
            , hour(EVENT_TIMESTAMP)     AS event_hr
        FROM VIEWS.SRP_EVENT_FACT
        WHERE
            SESSION_START_DT BETWEEN '{start_dt}' AND '{end_dt}'
            AND date(EVENT_TIMESTAMP) BETWEEN '{start_dt}' AND '{end_dt}'
    ) AS srp 
    INNER JOIN (
        SELECT DISTINCT user_id
        FROM P_DATA_T.ACCOUNTS_FLAG
        WHERE
            ind = 1 
    ) AS bad ON srp.user_id = bad.user_id 
) AS T
GROUP BY 1, 2
ORDER BY 1, 2
;

ALTER TABLE {table_name} ADD COLUMN last_modified_ts TIMESTAMP;

CONVERT TO DELTA {table_name};

UPDATE {table_name} SET last_modified_ts = CURRENT_TIMESTAMP()
