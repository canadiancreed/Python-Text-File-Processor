'''
Created on Sep 22, 2012

Handles all data access for application

@author: creed
'''
import MySQLdb


class Data:

    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host="localhost",
                               user="testPythonApp",
                               passwd="testPy",
                               db="testPythonAppDB"
                               )
            self.cursor = self.conn.cursor()
        except MySQLdb.Error, e:
            print "MySQLdb error %d: %s" % (e.args[0], e.args[1])
            return 0

    def insertData(self, table, dataArray):
        query = self.buildInsertQuery(table, dataArray)

        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception, e:
            self.conn.rollback()
            print "Unable to insert" + e

    def buildInsertQuery(self, table, dataArray):
        base = "INSERT INTO " + table + " ("
        tableFieldNames = dataArray[0]

        for titleRow in tableFieldNames:
            if tableFieldNames[-1] == titleRow:
                base = base + titleRow
            else:
                base = base + titleRow + ","

        del dataArray[0]

        base = base + ") VALUES "

        for line in dataArray:
            if line[0] != "Season" and line[0] != "Career":
                base = base + "("

                for data in line[:-1]:
                    base = base + str(data) + ','

                base = base + str(data) + ")"

        return base
