import sys
import sqlite3
from flight import Flight
class Flight_operations:    
    @staticmethod
    def connect_db():
        conn = sqlite3.connect('flights_db.db')
        return conn

    def create_table_flights():
        query = 'create table IF NOT EXISTS flights(id integer primary key AUTOINCREMENT, airline varchar(30) not null, source varchar(30) not null, destination varchar(30) not null, duration float, fare int)'
        conn = Flight_operations.connect_db()
        conn.execute(query)
        conn.close()
        print("Database is connected and in sync.")

    # def read_flight_details():
    #     airline = input('Enter airline name: ')
    #     source = input('Enter Source place name: ')
    #     destination = input('Enter Destination place name: ')
    #     duration = float(input('Enter Duration in hours: '))
    #     fare = float(input('Enter Fare in INR: '))
    #     return (airline, source, destination, duration, fare)

    # def create_flight():
    #     query = 'insert into flights(airline, source, destination, duration, fare) values(?, ?, ?, ?, ?)'
    #     conn = Flight_operations.connect_db()
    #     flight_details = read_flight_details()
    #     cursor = conn.cursor()
    #     cursor.execute(query, flight_details)
    #     id = cursor.lastrowid
    #     conn.commit()
    #     conn.close()
    #     return id
    def createFlight(flight):
        query = 'insert into flights(airline, source, destination, duration, fare) values(?, ?, ?, ?, ?)'
        params = (flight.airline, flight.source,flight.destination,flight.duration,flight.fare)
        con = Flight_operations.connect_db()
        cur = con.cursor()
        cur.execute(query,params)
        id = cur.lastrowid  #
        con.commit()
        con.close()
        return id    

    def search_flight(id):
        query = 'select * from flights where id = ?'
        # id = int(input('Enter id of the flight: '))
        conn = Flight_operations.connect_db()
        cursor = conn.cursor()
        response=cursor.execute(query, (id,))
        rs = response.fetchone()
        print(str(rs))
        if rs != None:
            flight = Flight(id=rs[0],airline=rs[1],
                    source=rs[2],destination=rs[3],duration=rs[4],fare=rs[5])
        else:
            flight = None 
        return flight
        

    def list_flights():
        query = 'select * from flights'
        conn = Flight_operations.connect_db()
        cursor = conn.cursor()
        response=cursor.execute(query)
        rows = response.fetchall()
        conn.close()
        flights = []
        for row in rows:
            flights.append(
                Flight(id=row[0], airline=row[1], source=row[2], destination=row[3], duration=row[4],fare=row[5])
            )
        # print(flights)
        return flights

    def delete_flight(id):
        query = 'delete from flights where (id=?)'
        # id = int(input('Enter id of the flight to be deleted: '))
        params = (id,)
        conn = Flight_operations.connect_db()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()

    def update_flight(flight):
        query = 'update flights set duration = ?, fare = ? where id = ?'
        # id = int(input('Enter id of the flight to be updated: '))
        # duration = float(input('Enter new duration of the flight: '))
        # fare = float(input('Enter new fare of the flight: '))
        params = (flight.duration, flight.fare,
              flight.id, )
        conn = Flight_operations.connect_db()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()
        return f'Updated Flight Successfully'

    def exit_program():
        sys.exit('End of App Execution')

    # def get_menu(choice):
    #     menu = {
    #         1 : create_table_flights,
    #         2 : create_flight,
    #         3 : update_flight,
    #         4 : delete_flight,
    #         5 : search_flight,
    #         6 : list_flights,
    #         7 : exit_program
    #     }
    #     return menu.get(choice, 'Invalid Choice')

# while True:
#     print('1:CreateTable 2:Insert 3:Update 4:Delete 5:Search 6:ListAll 7:Exit')
#     choice = int(input('Enter your choice: '))
#     my_function = get_menu(choice)
#     if my_function == 'Invalid Choice':
#         continue
#     my_function()