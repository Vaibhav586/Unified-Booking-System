import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Ipqul5849",
    database="UnifiedBookingSystem"
)
cursor = db_connection.cursor()

# Function to handle user login
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Placeholder logic for login verification
    query = "SELECT * FROM Users WHERE username = %s AND password_hash = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        user_id = user[0]  # Assuming user_id is the first column in the Users table
        main_window.withdraw()  # Hide the login window
        show_booking_options(user_id)  # Pass user_id to the show_booking_options function
    else:
        error_label.config(text="Invalid username or password")

# Function to show the booking options after login
def show_booking_options(user_id):
    booking_window = tk.Toplevel()  # Create a new window for booking options
    booking_window.title("Booking Options")

    # Buttons for booking options
    flight_button = ttk.Button(booking_window, text="Book Flight", command=lambda: book_flight_form(user_id))
    flight_button.pack(padx=10, pady=5)

    bus_button = ttk.Button(booking_window, text="Book Bus", command=lambda: book_bus_form(user_id))
    bus_button.pack(padx=10, pady=5)

    hotel_button = ttk.Button(booking_window, text="Book Hotel", command=lambda: book_hotel_form(user_id))
    hotel_button.pack(padx=10, pady=5)

    package_button = ttk.Button(booking_window, text="Book Package", command=lambda: book_package_form(user_id))
    package_button.pack(padx=10, pady=5)

# Function to show the flight booking form
# Function to show the flight booking form
def book_flight_form(user_id):
    flight_form_window = tk.Toplevel()  # Create a new window for flight booking form
    flight_form_window.title("Flight Booking Form")

    # Labels and entry fields for flight booking details
    from_label = ttk.Label(flight_form_window, text="From:")
    from_label.pack(padx=10, pady=5)
    from_entry = ttk.Entry(flight_form_window)
    from_entry.pack(padx=10, pady=5)

    to_label = ttk.Label(flight_form_window, text="To:")
    to_label.pack(padx=10, pady=5)
    to_entry = ttk.Entry(flight_form_window)
    to_entry.pack(padx=10, pady=5)

    departure_label = ttk.Label(flight_form_window, text="Departure Date:")
    departure_label.pack(padx=10, pady=5)
    departure_entry = ttk.Entry(flight_form_window)
    departure_entry.pack(padx=10, pady=5)

    return_label = ttk.Label(flight_form_window, text="Return Date:")
    return_label.pack(padx=10, pady=5)
    return_entry = ttk.Entry(flight_form_window)
    return_entry.pack(padx=10, pady=5)

    travel_label = ttk.Label(flight_form_window, text="Travel Class:")
    travel_label.pack(padx=10, pady=5)
    travel_combobox = ttk.Combobox(flight_form_window, values=["Economy", "Business", "First Class"])
    travel_combobox.pack(padx=10, pady=5)

    # Button to submit flight booking
    book_button = ttk.Button(flight_form_window, text="Book", command=lambda: book_flight(user_id, from_entry.get(), to_entry.get(), departure_entry.get(), return_entry.get(), travel_combobox.get()))
    book_button.pack(padx=10, pady=10)

    # Fetch results of previous query
    cursor.fetchall()  # Add this line to fetch the results of the previous query


# Function to handle flight booking and insert into Flights table
def book_flight(user_id, from_location, to_location, departure_date, return_date, travel_class):
    # Insert flight booking data into Flights table
    insert_query = "INSERT INTO Flights (user_id, from_location, to_location, departure_date, return_date, travel_class) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (user_id, from_location, to_location, departure_date, return_date, travel_class))
    db_connection.commit()

    print("Flight booked!")
    print("From:", from_location)
    print("To:", to_location)
    print("Departure Date:", departure_date)
    print("Return Date:", return_date)
    print("Travel Class:", travel_class)

# Function to show the bus booking form
def book_bus_form(user_id):
    bus_form_window = tk.Toplevel()  # Create a new window for bus booking form
    bus_form_window.title("Bus Booking Form")

    # Labels and entry fields for bus booking details
    from_label = ttk.Label(bus_form_window, text="From:")
    from_label.pack(padx=10, pady=5)
    from_entry = ttk.Entry(bus_form_window)
    from_entry.pack(padx=10, pady=5)

    to_label = ttk.Label(bus_form_window, text="To:")
    to_label.pack(padx=10, pady=5)
    to_entry = ttk.Entry(bus_form_window)
    to_entry.pack(padx=10, pady=5)

    travel_date_label = ttk.Label(bus_form_window, text="Travel Date:")
    travel_date_label.pack(padx=10, pady=5)
    travel_date_entry = ttk.Entry(bus_form_window)
    travel_date_entry.pack(padx=10, pady=5)

    # Button to submit bus booking
    book_button = ttk.Button(bus_form_window, text="Book", command=lambda: book_bus(user_id, from_entry.get(), to_entry.get(), travel_date_entry.get()))
    book_button.pack(padx=10, pady=10)

# Function to handle bus booking and insert into Buses table
def book_bus(user_id, from_location, to_location, travel_date):
    # Insert bus booking data into Buses table
    insert_query = "INSERT INTO Buses (user_id, from_location, to_location, travel_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (user_id, from_location, to_location, travel_date))
    db_connection.commit()

    print("Bus booked!")
    print("From:", from_location)
    print("To:", to_location)
    print("Travel Date:", travel_date)

# Function to show the hotel booking form
def book_hotel_form(user_id):
    hotel_form_window = tk.Toplevel()  # Create a new window for hotel booking form
    hotel_form_window.title("Hotel Booking Form")

    # Labels and entry fields for hotel booking details
    city_label = ttk.Label(hotel_form_window, text="City:")
    city_label.pack(padx=10, pady=5)
    city_entry = ttk.Entry(hotel_form_window)
    city_entry.pack(padx=10, pady=5)

    property_label = ttk.Label(hotel_form_window, text="Property Name or Location:")
    property_label.pack(padx=10, pady=5)
    property_entry = ttk.Entry(hotel_form_window)
    property_entry.pack(padx=10, pady=5)

    checkin_label = ttk.Label(hotel_form_window, text="Check-in Date:")
    checkin_label.pack(padx=10, pady=5)
    checkin_entry = ttk.Entry(hotel_form_window)
    checkin_entry.pack(padx=10, pady=5)

    checkout_label = ttk.Label(hotel_form_window, text="Check-out Date:")
    checkout_label.pack(padx=10, pady=5)
    checkout_entry = ttk.Entry(hotel_form_window)
    checkout_entry.pack(padx=10, pady=5)

    rooms_label = ttk.Label(hotel_form_window, text="Number of Rooms:")
    rooms_label.pack(padx=10, pady=5)
    rooms_entry = ttk.Entry(hotel_form_window)
    rooms_entry.pack(padx=10, pady=5)

    # Button to submit hotel booking
    book_button = ttk.Button(hotel_form_window, text="Book", command=lambda: book_hotel(user_id, city_entry.get(), property_entry.get(), checkin_entry.get(), checkout_entry.get(), rooms_entry.get()))
    book_button.pack(padx=10, pady=10)

# Function to handle hotel booking and insert into Hotels table
def book_hotel(user_id, city, property_name, checkin_date, checkout_date, rooms):
    # Insert hotel booking data into Hotels table
    insert_query = "INSERT INTO Hotels (user_id, city, property_name, checkin_date, checkout_date, rooms) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (user_id, city, property_name, checkin_date, checkout_date, rooms))
    db_connection.commit()

    print("Hotel booked!")
    print("City:", city)
    print("Property Name or Location:", property_name)
    print("Check-in Date:", checkin_date)
    print("Check-out Date:", checkout_date)
    print("Number of Rooms:", rooms)

# Function to show the package booking form
def book_package_form(user_id):
    package_form_window = tk.Toplevel()  # Create a new window for package booking form
    package_form_window.title("Package Booking Form")

    # Labels and entry fields for package booking details
    city_label = ttk.Label(package_form_window, text="City:")
    city_label.pack(padx=10, pady=5)
    city_entry = ttk.Entry(package_form_window)
    city_entry.pack(padx=10, pady=5)

    property_label = ttk.Label(package_form_window, text="Property Name or Location:")
    property_label.pack(padx=10, pady=5)
    property_entry = ttk.Entry(package_form_window)
    property_entry.pack(padx=10, pady=5)

    checkin_label = ttk.Label(package_form_window, text="Check-in Date:")
    checkin_label.pack(padx=10, pady=5)
    checkin_entry = ttk.Entry(package_form_window)
    checkin_entry.pack(padx=10, pady=5)

    checkout_label = ttk.Label(package_form_window, text="Check-out Date:")
    checkout_label.pack(padx=10, pady=5)
    checkout_entry = ttk.Entry(package_form_window)
    checkout_entry.pack(padx=10, pady=5)

    rooms_label = ttk.Label(package_form_window, text="Number of Rooms:")
    rooms_label.pack(padx=10, pady=5)
    rooms_entry = ttk.Entry(package_form_window)
    rooms_entry.pack(padx=10, pady=5)

    from_label = ttk.Label(package_form_window, text="From:")
    from_label.pack(padx=10, pady=5)
    from_entry = ttk.Entry(package_form_window)
    from_entry.pack(padx=10, pady=5)

    to_label = ttk.Label(package_form_window, text="To:")
    to_label.pack(padx=10, pady=5)
    to_entry = ttk.Entry(package_form_window)
    to_entry.pack(padx=10, pady=5)

    travel_label = ttk.Label(package_form_window, text="Travel Date:")
    travel_label.pack(padx=10, pady=5)
    travel_entry = ttk.Entry(package_form_window)
    travel_entry.pack(padx=10, pady=5)

    # Button to submit package booking
    book_button = ttk.Button(package_form_window, text="Book", command=lambda: book_package(user_id, city_entry.get(), property_entry.get(), checkin_entry.get(), checkout_entry.get(), rooms_entry.get(), from_entry.get(), to_entry.get(), travel_entry.get()))
    book_button.pack(padx=10, pady=10)

# Placeholder function for package booking
def book_package(user_id, city, property_name, checkin_date, checkout_date, rooms, from_location, to_location, travel_date):
    # Insert package booking data into Packages table
    insert_query = "INSERT INTO Packages (user_id, city, property_name, checkin_date, checkout_date, rooms, from_location, to_location, travel_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (user_id, city, property_name, checkin_date, checkout_date, rooms, from_location, to_location, travel_date))
    db_connection.commit()

    print("Package booked!")
    print("City:", city)
    print("Property Name or Location:", property_name)
    print("Check-in Date:", checkin_date)
    print("Check-out Date:", checkout_date)
    print("Number of Rooms:", rooms)
    print("From:", from_location)
    print("To:", to_location)
    print("Travel Date:", travel_date)

# Create main application window
main_window = tk.Tk()
main_window.title("Unified Booking System")

# Create frame for login form
frame = ttk.Frame(main_window)
frame.pack(padx=20, pady=20)

# Labels and entry fields for username and password
username_label = ttk.Label(frame, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = ttk.Entry(frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = ttk.Label(frame, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = ttk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Error label for displaying login errors
error_label = ttk.Label(frame, text="", foreground="red")
error_label.grid(row=2, columnspan=2, padx=5, pady=5)

# Button to login
login_button = ttk.Button(frame, text="Login", command=login)
login_button.grid(row=3, columnspan=2, padx=5, pady=5)

main_window.mainloop()
