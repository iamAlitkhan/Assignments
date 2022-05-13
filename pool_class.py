import datetime

pool_tables = []


class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.check_out_time = None
        self.check_in_time = None
        self.time_played = None
        self.is_occupied = False

    def check_out(self):
        self.is_occupied = True
        self.check_out_time = datetime.datetime.now()

    def check_in(self):
        self.is_occupied = False
        self.check_in_time = datetime.datetime.now()
