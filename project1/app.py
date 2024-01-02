import tkinter as tk
import requests

def send_to_api():
    data = {
        "name": name_entry.get(),
        "age": age_entry.get(),
        "city": city_entry.get()
    }
    response = requests.post('http://127.0.0.1:5000/api/data', json=data)
    result_label.config(text=response.json()["message"])

root = tk.Tk()
root.title("Tkinter App with Flask and MongoDB")

# Entry Widgets
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Button to send data
send_button = tk.Button(root, text="Send Data", command=send_to_api)
send_button.pack()

# Display result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()