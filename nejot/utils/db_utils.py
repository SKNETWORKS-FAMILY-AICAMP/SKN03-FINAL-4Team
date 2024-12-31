import pymysql
from nejot.config import DB_CONFIG

def fetch_all_from_db(db_config):
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM UserBenchmarks")
            rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"DB 데이터 가져오기 오류: {e}")
        return None
    finally:
        connection.close()


def insert_or_update_spec_info(db_config, spec, web_info):
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            check_sql = "SELECT COUNT(*) as cnt FROM UserBenchmarks WHERE Model = %s"
            cursor.execute(check_sql, (spec,))
            result = cursor.fetchone()
            count = result['cnt']

            if count > 0:
                update_sql = "UPDATE UserBenchmarks SET information = %s WHERE Model = %s"
                cursor.execute(update_sql, (web_info, spec))
                print(f"'{spec}'에 대한 웹 검색 결과를 기존 레코드에 UPDATE했습니다.")
            else:
                insert_sql = """
                    INSERT INTO `UserBenchmarks` (`Type`, `Brand`, `Model`, `Rank`, `Benchmark`, `URL`, `information`)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_sql, (None, None, spec, None, None, None, web_info))
                print(f"'{spec}' 스펙이 DB에 없으므로 새로운 레코드를 INSERT했습니다.")

        connection.commit()
    except Exception as e:
        print(f"웹 정보 DB 저장 오류: {e}")
    finally:
        connection.close()
