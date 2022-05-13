
from pool_class import *

pool_tables = []
number_of_tables = 12

for i in range(1, number_of_tables + 1):
    pool_table = PoolTable(i)
    pool_tables.append(pool_table)
# all_tables = (pool_tables[i - 1].table_number)
# print(all_tables)
while True:
    print('''
    Press 1 to view all tables:
    Press 2 to check out a table:
    Press 3 to check in a table:
    Press q to  quit:
    ''')

    choice = input("Enter choice: ")

    if choice == "1":
        for table in pool_tables:
            if table.is_occupied == False:
                print(f"This table {table.table_number} is available")
            if table.is_occupied == True:
                print(f"This table {table.table_number} is occupied")
    if choice == "2":
        for table in pool_tables:
            if table.is_occupied == False:
                print(f"This table {table.table_number} is available")
            if table.is_occupied == True:
                print(
                    f"Table {table.table_number} Check out time: {table.check_out_time}")
        choice = int(input("Which table do you want to check out? "))
        table = pool_tables[choice - 1]
        table.check_out()

    if choice == "3":
        for table in pool_tables:
            if table.is_occupied == True:
                print(f"This table {table.table_number} is occupied")
            if table.is_occupied == False:
                print(
                    f"Table {table.table_number} Check in time: {table.check_in_time}")
                duration = {table.check_out_time} - {table.check_in_time}
                print(
                    f"Duration of play: {duration}")
        choice = int(input("Which table do you want to check in? "))
        table = pool_tables[choice - 1]
        table.check_in()

    if choice == "q":
        break
