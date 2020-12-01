import cx_Oracle


class DBSessionPool:
    pool: cx_Oracle.SessionPool
    conn: cx_Oracle.Connection

    def __init__(self, pool: cx_Oracle.SessionPool):
        self.pool = pool

    def __enter__(self) -> cx_Oracle.Connection:
        self.conn = self.pool.acquire()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.release(self.conn)
