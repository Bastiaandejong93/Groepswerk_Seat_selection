import tkinter as tk
import mysql.connector
#from PIL import ImageTk
from tkinter import *
from tkinter import messagebox

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Menu voor employees
        employeeMenu = Menu(menu)
        employeeMenu.add_command(label="Add employee", command=self.add_employee)
        employeeMenu.add_command(label="Delete employee", command=self.delete_employee)
        employeeMenu.add_command(label="Reform employee", command=self.reform_employee)
        menu.add_cascade(label="Employees", menu=employeeMenu)

        # Menu voor rooms
        roomMenu = Menu(menu)
        roomMenu.add_command(label="Add room", command=self.add_room)
        roomMenu.add_command(label="Delete room", command=self.delete_room)
        roomMenu.add_command(label="Reform room", command=self.reform_room)
        menu.add_cascade(label="Rooms", menu=roomMenu)

        # Menu voor Customers
        customerMenu = Menu(menu)
        customerMenu.add_command(label="Add customer", command=self.add_customer)
        customerMenu.add_command(label="Delete customer", command=self.delete_customer)
        customerMenu.add_command(label="Reform customer", command=self.reform_customer)
        menu.add_cascade(label="Customers", menu=customerMenu)

        # Menu voor Movies
        movieMenu = Menu(menu)
        movieMenu.add_command(label="Add movie", command=self.add_movie)
        movieMenu.add_command(label="Delete movie", command=self.delete_movie)
        movieMenu.add_command(label="Reform movie", command=self.reform_movie)
        menu.add_cascade(label="Movies", menu=movieMenu)

        # Menu voor bewerken
        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        self.master.config(menu=menu)

        self.db_connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        self.db_cursor = self.db_connection.cursor()
    def exitProgram(self):
        exit()
    def add_employee(self):
        employee_name = input("Enter employee name: ")
        employee_position = input("Enter employee position: ")

        # Voeg de werknemer toe aan de database
        query = "INSERT INTO employees (name, position) VALUES (%s, %s)"
        values = (employee_name, employee_position)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Employee added successfully.")

    def delete_employee(self):
        employee_id = input("Enter employee ID to delete: ")

        # Verwijder de werknemer uit de database
        query = "DELETE FROM employees WHERE id = %s"
        values = (employee_id,)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Employee deleted successfully.")
    def reform_employee(self):
        employee_id = input("Enter employee ID to update: ")
        new_name = input("Enter new name for the employee: ")
        new_position = input("Enter new position for the employee: ")

        # Bewerk de werknemer in de database
        query = "UPDATE employees SET name = %s, position = %s WHERE id = %s"
        values = (new_name, new_position, employee_id)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Employee updated successfully.")
    def add_room(self):
        room_number = input("Enter room number: ")
        room_type = input("Enter room type: ")
        room_capacity = input("Enter room capacity: ")
        # Voeg de kamer toe aan de database
        query = "INSERT INTO rooms (room_number, room_type, room_capacity) VALUES (%s, %s, %s)"
        values = (room_number, room_type, room_capacity)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Room added successfully.")
    def delete_room(self):
        room_id = input("Enter room ID to delete: ")

        # Verwijder de kamer uit de database
        query = "DELETE FROM rooms WHERE id = %s"
        values = (room_id,)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Room deleted successfully.")
    def reform_room(self):
        room_id = input("Enter room ID to update: ")
        new_room_number = input("Enter new room number: ")
        new_room_type = input("Enter new room type: ")
        new_room_capacity = input("Enter new room capacity: ")

        # Bewerk de kamer in de database
        query = "UPDATE rooms SET room_number = %s, room_type = %s, room_capacity = %s WHERE id = %s"
        values = (new_room_number, new_room_type, new_room_capacity, room_id)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Room updated successfully.")
    def add_customer(self):
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email: ")
        customer_phone = input("Enter customer phone number: ")

        # Voeg de klant toe aan de database
        query = "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"
        values = (customer_name, customer_email, customer_phone)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Customer added successfully.")


def delete_customer(self):
    customer_id = input("Enter customer ID to delete: ")

    # Verwijder de klant uit de database
    query = "DELETE FROM customers WHERE id = %s"
    values = (customer_id,)
    self.db_cursor.execute(query, values)
    self.db_connection.commit()

    print("Customer deleted successfully.")

    def reform_customer(self):
        customer_id = input("Enter customer ID to update: ")
        new_name = input("Enter new name for the customer: ")
        new_email = input("Enter new email for the customer: ")
        new_phone = input("Enter new phone number for the customer: ")

        # Bewerk de klant in de database
        query = "UPDATE customers SET name = %s, email = %s, phone = %s WHERE id = %s"
        values = (new_name, new_email, new_phone, customer_id)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Customer updated successfully.")

    def add_movie(self):
        movie_title = input("Enter movie title: ")
        movie_genre = input("Enter movie genre: ")
        movie_release_date = input("Enter movie release date: ")

        # Voeg de film toe aan de database
        query = "INSERT INTO movies (title, genre, release_date) VALUES (%s, %s, %s)"
        values = (movie_title, movie_genre, movie_release_date)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Movie added successfully.")
    def delete_movie(self):
        movie_id = input("Enter movie ID to delete: ")

        # Verwijder de film uit de database
        query = "DELETE FROM movies WHERE id = %s"
        values = (movie_id,)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Movie deleted successfully.")

    def reform_movie(self):
        movie_id = input("Enter movie ID to update: ")
        new_title = input("Enter new title for the movie: ")
        new_genre = input("Enter new genre for the movie: ")
        new_release_date = input("Enter new release date for the movie: ")

        # Bewerk de film in de database
        query = "UPDATE movies SET title = %s, genre = %s, release_date = %s WHERE id = %s"
        values = (new_title, new_genre, new_release_date, movie_id)
        self.db_cursor.execute(query, values)
        self.db_connection.commit()

        print("Movie updated successfully.")



root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.mainloop()
