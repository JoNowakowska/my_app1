import sqlite3
import datetime


class InteractionsWithDb:
    @classmethod
    def insert_to_db(cls, new_entry):
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        create_table = "CREATE TABLE IF NOT EXISTS diary (DATE text, EVENT text)"
        cursor.execute(create_table)
        query = "INSERT INTO diary VALUES (?, ?)"
        cursor.execute(query, (date, new_entry))
        connection.commit()
        connection.close()

    @classmethod
    def select_all_from_db(cls):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        select_all = "SELECT * FROM diary"
        results = cursor.execute(select_all)

        return results.fetchall()
