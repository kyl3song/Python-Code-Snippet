# -*- coding: utf-8 -*-
# @Author: Kyle Song (fkilla8210@gmail.com)
# @Date:   2020-03-02 19:10:12
# @Last Modified by:   KyleSong

import sqlite3


def main():
    """ Basic usage of sqlite """
    db_file = 'sqlite.db'

    conn = get_sqlite_conn(db_file)
    cur = conn.cursor()

    # If table already exists, "table [table_name] already exists" error occurs
    cur.execute("DROP TABLE IF EXISTS dfir")

    cur.execute("CREATE TABLE dfir(filename text, type text, size int, username char(20))")

    cur.execute("INSERT INTO dfir values('a.exe', 'exe', 14579664, 'admin')")
    cur.execute("INSERT INTO dfir values('b.png', 'png', 2200, 'admin')")
    cur.execute("INSERT INTO dfir values('c.mov', 'mov', 154700, 'kyle')")

    sql_insert = "INSERT INTO dfir(filename, type, size, username) values (?, ?, ?, ?)"
    data = ["forensics.txt", "txt", 500, "kyle"]
    cur.execute(sql_insert, data)

    conn.commit()

    # Returns output with list of tuples (fetchmany(n) / fetchone() / fetchall())
    db_select = cur.execute("SELECT * FROM dfir")
    db_select = cur.fetchmany(2)
    print(db_select)

    db_select = cur.execute("SELECT * FROM dfir")
    db_select = cur.fetchall()
    print(db_select)

    db_count = cur.execute("SELECT COUNT(*) FROM dfir")
    db_count = cur.fetchall()
    print(db_count)

    cur.close()
    conn.close()


def get_sqlite_conn(db_file):
    """ Make connection to SQLite database and returns connection handler """
    conn = sqlite3.connect(db_file)
    return conn


if __name__ == '__main__':
    main()
