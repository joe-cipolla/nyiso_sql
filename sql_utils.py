"""sql worker functions and queries"""

import psycopg2
import pandas as pd
import nyiso_sql.global_vars as gvars


conn_closed_msg = "PostgreSQL connection is close."


def insert_row(table_name, record, conn=None, pkey_id=None, cur=None):
    """ inserts single row into table
    :param table_name - string
    :param record - list of tuples
    :param conn - db connection
    :param pkey_id - primary key
    :param cur - db cursor
    """

    sql = gvars.sql_insert_map[table_name]

    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.execute(sql, record)
        pkey_id = cur.fetchone()[0]
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print(conn_closed_msg)

    return pkey_id


def bulk_insert_rows(table_name, records, conn=None, cur=None, print_msg=False):
    """ inserts multiple rows into table
    :param table_name - string
    :param records - list of tuples, each with length = number of columns in table
    :param conn - db connection
    :param cur - db cursor
    :param print_msg - boolean, whether or not to print messages
    """

    sql = gvars.sql_insert_map[table_name]

    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.executemany(sql, records)
        conn.commit()
        if print_msg:
            print(cur.rowcount, "Record inserted successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn:
            cur.close()
            conn.close()
            if print_msg:
                print(conn_closed_msg)


def drop_row(table_name, row_id, conn=None, cur=None):
    """drops all rows from table matching row_ids
    :param table_name - string
    :param row_id - int
    :param conn - db connection
    :param cur - db cursor
    """

    sql = gvars.sql_drop_map[table_name]
    
    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.execute(sql, (row_id, ))
        conn.commit()
        print(cur.rowcount, "Record deleted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print(conn_closed_msg)


def bulk_drop_rows(table_name, row_ids, conn=None, cur=None):
    """drops all rows from table matching row_ids
    :param table_name - string
    :param row_ids - list of tuples
    :param conn - db connection
    :param cur - db cursor
    """

    sql = gvars.sql_drop_map[table_name]
    
    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.executemany(sql, row_ids)
        conn.commit()
        print(cur.rowcount, "Record deleted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print(conn_closed_msg)


def lookup_value_in_table(lookup_type, lookup_input, conn=None, cur=None):
    """ looks up single value id or name from dim mapping tables, using sql queries in global_vars.py
    :param lookup_type - str, value to be looked up in table
    :param lookup_input - value to be mapped to find lookup value
    :param conn - database connection
    :param cur - connection cursor
    :return lookup_value - str/int/etc.
    """

    sql = gvars.sql_lookup_map[lookup_type]

    lookup_value = None
    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        cur = conn.cursor()
        cur.execute(sql, (lookup_input, ))
        lookup_value = cur.fetchall()[0][0]
    except (Exception, psycopg2.Error) as error:
        print("Error in Select operation", error)
    finally:
        if conn:
            cur.close()
            conn.close()

    return lookup_value


def check_if_dst(date, conn=None):
    """ checks if date is dst start_date or end_date in vw_dst view
    :param date - str, YYYY-MM-DD
    :param conn - database connection
    :return is_dst - 2 value tuple containing 0 or 1 boolen for start and end date (start_date_is_dst, end_date_is_dst)
    i.e. (0, 1) if date is a dst end_date
    """

    sql = """SELECT * FROM vw_dst"""
    try:
        conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                                user=gvars.t_user, password=gvars.t_pw)
        dst = pd.read_sql(sql, conn)
    except (Exception, psycopg2.Error) as error:
        print("Error in Select operation", error)
    finally:
        if conn:
            conn.close()

    is_dst = (0, 0)
    if pd.to_datetime(date) in dst.start_date.tolist():
        is_dst = (1, 0)
    elif pd.to_datetime(date) in dst.end_date.tolist():
        is_dst = (0, 1)

    return is_dst


def check_if_date_in_table(date_id, data_type):

    sql = gvars.select_datatype_by_date_id[data_type]
    sql = sql.replace('%s', date_id)

    conn = psycopg2.connect(host=gvars.t_host, port=gvars.t_port, dbname=gvars.t_dbname,
                            user=gvars.t_user, password=gvars.t_pw)
    df = pd.read_sql(sql, conn)
    date_in_table = False
    if df.__len__() != 0:
        date_in_table = True

    return date_in_table


if __name__ == '__main__':
    insert_row(
        'da_lmp',
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    )
    
    bulk_insert_rows(
        'da_lmp',
        [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
          0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01),
         (1, 1, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50,
          0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50),
         (1, 1, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
          100, 100, 100, 100, 100, 100, 100, 100, 100, 100)]
    )

    drop_row('da_lmp', 13)
    bulk_drop_rows('da_lmp', [(2, ), (3, ), (4, ), (5, )])
