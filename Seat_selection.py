import tkinter as tk
from CLASS_BIOS import Room
import csv
from tkinter import messagebox

# Functie die wordt aangeroepen wanneer een stoel wordt geklikt
def seat_click(row, seat):
    if seat_status[row][seat] == "empty":
        seat_status[row][seat] = "selected"
        seats[row][seat].configure(bg="green")
    else:
        seat_status[row][seat] = "empty"
        seats[row][seat].configure(bg="white")
    root.update()

# Functie voor het afrekenen van de geselecteerde stoelen
def checkout():
    selected_seats = []
    for row in range(seat_rows):
        for seat in range(seat_columns):
            if seat_status[row][seat] == "selected":
                selected_seats.append((row, seat))

    if len(selected_seats) > 0:
        show_overview(selected_seats)
    else:
        messagebox.showwarning("No Seats", "You haven't selected any seats.")

# Functie voor het weergeven van het overzicht van de bestelling
def show_overview(selected_seats):
    overview_window = tk.Toplevel(root)
    overview_window.title("Order Overview")
    overview_window.geometry("400x400")

    seat_numbers = ", ".join([f"{chr(65+row)}{column + 1}" for row, column in selected_seats])
    total_price = (len(selected_seats) * 10)

    seats_label = tk.Label(overview_window, text="Selected Seats:")
    seats_label.pack()

    seats_text = tk.Text(overview_window, height=10, width=30)
    seats_text.insert(tk.END, seat_numbers)
    seats_text.config(state="disabled")
    seats_text.pack()

    price_label = tk.Label(overview_window, text="Total Price:")
    price_label.pack()

    price_text = tk.Text(overview_window, height=1, width=10)
    price_text.insert(tk.END, f"€{total_price}")
    price_text.config(state="disabled")
    price_text.pack()

    proceed_button = tk.Button(overview_window, text="Proceed to Payment", command=proceed_payment)
    proceed_button.pack()

    pay_counter_button = tk.Button(overview_window, text="Pay at the Counter", command=lambda: pay_counter(selected_seats))
    pay_counter_button.pack()

# Functie voor het verwerken van betaling
def proceed_payment():
    messagebox.showinfo("Payment", "Payment currently not available. Please select 'Pay at the Counter'.")

# Functie voor betalen bij de balie
def pay_counter(selected_seats):
    for seat in selected_seats:
        row, col = seat
        seats[row][col]["bg"] = "red"
        seats[row][col]["state"] = "disabled"
    messagebox.showinfo("Reservation", "Reservation Confirmed. Please pay at the counter.")
    save_reservation(selected_seats)

# Functie voor terugkeren naar de vorige pagina
def go_back():
    root.quit()

# Functie voor het laden van reserveringen uit het CSV-bestand
def load_reservations():
    with open("reservations_final.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reservations = list(reader)

    # Disable de gereserveerde stoelen
    for reservation in reservations:
        try:
            row = int(reservation[1])
            col = int(reservation[2])
            seats[row][col].configure(state="disabled", bg="red")
        except (IndexError, ValueError):
            pass  # Als de reserveringsinformatie niet geldig is, slaan we het over

    return reservations

# Functie voor het opslaan van de geselecteerde stoelen als reserveringen in het CSV-bestand
def save_reservation(selected_seats):
    with open("reservations_final.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for seat in selected_seats:
            row, col = seat
            writer.writerow([seats[row][col].name, row, col])

#######################################################
# GUI
#######################################################

root = tk.Tk()
root.title("Cinema Seat Reservation")
root.geometry("800x800")
root.configure(bg="grey")

seat_rows = 10
seat_columns = 10

seats_frame = tk.Frame(root, bg="gray")
seats_frame.pack(fill="both", expand=True, padx=10, pady=10)

seat_status = [["empty" for _ in range(seat_columns)] for _ in range(seat_rows)]
seats = []

# Maak stoelen aan en voeg ze toe aan de GUI
for row in range(seat_rows):
    seat_row = []
    for column in range(seat_columns):
        room = Room("Zaal 1", row, column, row, column)
        seat = tk.Button(seats_frame, text=f"{chr(65+row)}{column + 1}", bg="white", state="normal")
        seat.name = room.name
        seat.row = room.row
        seat.seat = room.seat
        seat["command"] = lambda btn=seat: seat_click(int(btn.row), int(btn.seat))
        seat.grid(row=row, column=column, padx=7, pady=7, ipadx=5, ipady=5)
        seat_row.append(seat)
    seats.append(seat_row)

# Scherm
header_frame = tk.Frame(root, bg="black", height=50)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="Scherm", fg="white", bg="black")
header_label.pack()

root.grid_rowconfigure(seat_rows, weight=1)
root.grid_columnconfigure(seat_columns-1, weight=1)

checkout_button = tk.Button(root, text="Checkout", command=checkout)
checkout_button.pack(side="right", padx=5, pady=10)

back_button = tk.Button(root, text="Terug", command=go_back)
back_button.pack(side="left", padx=5, pady=10)

load_reservations()  # Laad reserveringen en schakel gereserveerde stoelen uit
root.mainloop()
