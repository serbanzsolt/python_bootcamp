import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

#*With cursor object, communication with the database is set
#*Commands will be executed with cursor object

#*create new table
#*create table (column1 column_type, column2_column_type , column3_column_type...)
#*column types: string=text, int=integer, float=real, binary=blob

cursor.execute("create table gta (release_year integer, release_name text, city text)")

#(relese year, release name, city where the story happens)
release_list = [
    (1997, "GTA", "state of New Guernsey"),
    (1999, "GTA 2", "Anywhere, USA"),
    (2001, "GTA 3", "Liberty City"),
    (2002, "GTA: Vice City", "Vice City"),
    (2004, "GTA: San Andreas", "state of San Andreas"),
    (2008, "GTA 4", "Liberty City"),
    (2013, "GTA 5", "Los Santos")
]

#* insert can be made after the existance of the table
#* multiple rows can be added by executemany()
#* (?,?,?) this will be the stucture of the data, like a tamplate
cursor.executemany("insert into gta values (?,?,?)", release_list)

#*Printing the rows of the databse
for row in cursor.execute("select * from gta"):
    print(row)

#*Printing a specific row
print("------------------------------------------------")
cursor.execute("select * from gta where city=:C", {"C" : "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

#*creating the 2nd table
cursor.execute("create table cities (gta_city text, real_city text)")
cursor.execute("insert into cities values (?,?)", ("Liberty City", "New York"))
cursor.execute("select * from cities where gta_city=:C", {"C" : "Liberty City"})
cities_search = cursor.fetchall()
print(cities_search)

print("------------------------------------------------")
#*Manipulate database data
#*Replace all "Liberty City" with the real city name "New York"
for i in gta_search:
    adjusted = [cities_search[0][1] if value==cities_search[0][0] else value for value in i]
    print(adjusted)

connection.close()