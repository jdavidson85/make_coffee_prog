import sqlite3


def main():
    my_db = None
    try:
        my_db = sqlite3.connect('coffee.db')
        my_cursor = my_db.cursor()
        table_structure = """Create TABLE IF NOT EXISTS Coffee
                            (ProductID INTEGER PRIMARY KEY NOT NULL,
                            Product TEXT, Category TEXT, Supplier TEXT)"""
        my_cursor.execute(table_structure)
        my_db.commit()

        try:
            data_file = open("coffeehouse_suppliers.csv", "r")
            count = 0
            for line in data_file:
                data = line.strip().split(",")
                my_cursor.execute("""INsert INTO Coffee (Product, Category, Supplier)
                Values (?, ?, ?)""", (data[0],data[1], data[2]))

                count += 1

            print(f"{count} records added")
            data_file.close()
            my_db.commit()
        except IndexError:
            print("Error: Data file not found")
        except IDError:
            print("Error Unable to find data to coffee house suppliers")
        except sqlite3.Error:
            print("Error Encountered")

        except sqlite3.Error:
            print("SSQL Error encountered")
        finally:
            if my_db is not None:
                my_db.close()

main()
        