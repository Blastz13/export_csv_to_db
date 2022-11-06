from dask import dataframe as dd
from progress.bar import IncrementalBar
import logging
import sqlite3
import time


def read_csv(url: str) -> list[tuple]:
    dask_df = dd.read_csv(url)
    count_lines = len(dask_df)

    bar = IncrementalBar('Progress bar', max=count_lines)

    data_to_db = []
    for data_frame in dask_df.itertuples(index=False):
        data_to_db.append((data_frame[0], data_frame[1], data_frame[2], data_frame[3], data_frame[4],
                           data_frame[5], data_frame[6], data_frame[7], data_frame[8], data_frame[9],
                           data_frame[10], data_frame[11], data_frame[12], data_frame[13]))
        bar.next()
    bar.finish()
    return data_to_db


def upload_to_db(url: str, data: list[tuple]) -> int:
    try:
        connection = sqlite3.connect(url)
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS "incident_api_incident" 
        ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "crime_id" integer NOT NULL, 
        "original_crime_type_name" text NOT NULL, "report_date" datetime NOT NULL, 
        "call_date" datetime NOT NULL, "offense_date" datetime NOT NULL, "call_time" datetime NOT NULL, 
        "call_date_time" datetime NOT NULL, "disposition" text NOT NULL, "address" text NOT NULL, "city" text NULL, 
        "state" text NOT NULL, "agency_id" integer NOT NULL, "address_type" text NOT NULL, "common_location" text NULL);
        ''')
        cursor.execute(
            '''CREATE INDEX IF NOT EXISTS "incident_api_incident_report_date_fafaa8af"
            ON "incident_api_incident" ("report_date");''')
        connection.commit()

        cursor.executemany(
            "INSERT INTO incident_api_incident ('crime_id', 'original_crime_type_name','report_date', 'call_date', "
            "'offense_date','call_time', 'call_date_time', 'disposition', 'address', 'city', 'state', 'agency_id', "
            "'address_type', 'common_location') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);",
            data)
        connection.commit()
        count_created_rows = cursor.execute("SELECT COUNT(*) FROM incident_api_incident;").fetchone()[0]
    except Exception as e:
        logging.error(e)
    finally:
        cursor.close()

    return count_created_rows


if __name__ == '__main__':
    file_log = logging.FileHandler('upload_data_to_db.log')
    console_out = logging.StreamHandler()
    logging.basicConfig(handlers=(file_log, console_out),
                        format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)

    start = time.time()
    data = read_csv('police-department-calls-for-service.csv')
    count_created_rows = upload_to_db("db.sqlite3", data)

    logging.info(f" Created {count_created_rows} rows")
    logging.info("-— %s seconds —-" % (time.time() - start))
