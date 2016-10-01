# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb

class TeraQATakeLeave:
    cursor = None
    db = None

    def __init__(self, host, username, password, database):
        self.db = MySQLdb.connect(host, username, password, database)
        self.cursor = self.db.cursor()

    def list_all_data(self):
        self.cursor.execute("select id, name, `time-from`, `time-end` from takeleave.teraQA;")
        data = self.cursor.fetchall()
        for i in data:
            print i

    def list_select_name(self, name):
        self.cursor.execute("select id, name, `time-from`, `time-end` from takeleave.teraQA where `name`=\'{0}\';".format(name))
        data = self.cursor.fetchall()
        for i in data:
            print i

    def insert_data(self, name, time_from, time_end):
        self.cursor.execute("insert takeleave.teraQA(name, `time-from`, `time-end`) values(\'{0}\', \'{1}\', \'{2}\');".format(name, time_from, time_end))
        self.db.commit()

    def update_data(self, leave_id, time_from, time_end):
        self.cursor.execute("update takeleave.teraQA SET `time-from`=\'{0}\', `time-end`=\'{1}\' WHERE `id`=\'{2}\';".format(time_from, time_end, leave_id))
        self.db.commit()

    def delete_data_from_id(self, leave_id):
        self.cursor.execute("delete from takeleave.teraQA where `id`={0};".format(leave_id))
        self.db.commit()

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    pass
