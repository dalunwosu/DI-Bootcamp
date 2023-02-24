import psycopg2
USERNAME = "postgres"
PASSWORD = "daza"
DATABASE = "restaurant"
HOSTNAME = "localhost"

connection = psycopg2.connect(
    host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

cursor = connection.cursor()


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = f"insert into menu (name,price) values ('{self.name}',{self.price});"
        run_query(query)

    def delete(self):
        query = f"delete from menu where name = '{self.name}';"
        run_query(query)

    def update_price(self, new_price):
        query = f"update menu set price = {new_price};"
        run_query(query)

    def update_name(self, new_name):
        query = f"update menu set name = {new_name} where name = '{self.name}';"
        run_query(query)

    def all(self):
        query = "select name,price from menu;"
        return run_query(query)
    
    def __repr__(self):
            return f"({self.name},{self.price})"



def run_query(query):
    cursor.execute(query)
    output = None
    try:
        output = cursor.fetchall()
    except:
        connection.commit()

    return output


if __name__ == "__main__":
    burger = MenuItem('Burger', 10)
    burger.save()
