import sqlite3

from lib.lib import fn

class Database():

    def __init__(self):
        self.con = sqlite3.connect('test.db')
        print(fn())

if __name__ == '__main__':
    d = Database()
    print(d)