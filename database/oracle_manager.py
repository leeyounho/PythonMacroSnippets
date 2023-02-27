from sqlalchemy import create_engine, text
import pandas as pd


class OracleManager:
    def __init__(self, user, password, ip, port, service_name):
        self.engine = create_engine('oracle://' + user + ':' + password + '@' + ip + ':' + port + '/' + service_name)

    # engine = create_engine('oracle+cx_oracle://scott:tiger@tnsname')
    def get_dataframe_from_query(self, query):
        with self.engine.connect() as conn:
            return pd.read_sql_query(text(query), conn)


if __name__ == '__main__':
    oracle_manager = OracleManager('scott', 'tiger', '127.0.0.1', '1521', 'yhorcl')
    print(oracle_manager.get_dataframe_from_query("""select * from regions"""))