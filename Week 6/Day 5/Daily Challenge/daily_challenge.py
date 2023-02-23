import requests
import random
import psycopg2
import json

url = requests.get("https://restcountries.com/v3.1/all")
countries = url.json()

USERNAME = "postgres"
PASSWORD = "daza"
DATABASE = "countries"
HOSTNAME = "localhost"

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()

for i in range(10):
    rnd = random.randint(0, 195)
    name = countries[rnd]['name']['common']
    capital = countries[rnd]['capital'][0]
    flag = countries[rnd]['flag']
    subregion = countries[rnd]['subregion']
    population = countries[rnd]['population']
    cursor.execute(f"insert into countries (name,capital,sub_region,flag,population) values ('{name}','{capital}','{subregion}', '{flag}', '{population}')")
connection.commit()
connection.close()


