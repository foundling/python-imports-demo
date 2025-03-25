import sqlite3

from lib.lib import fn
from sibling import sibling_f

class Database():

    def __init__(self):
        self.con = sqlite3.connect('test.db')
        print(fn())
        print(sibling_f())

if __name__ == '__main__':
    d = Database()
    print(d)