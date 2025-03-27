CHATGPT CONVERSATION

************

add a GUI to this code

----------

class KPI:
    def __init__(self, name, target):
        self.name = name
        self.target = target

class KPIApp:
    def __init__(self):
        self.kpis = []

    def add_kpi(self, name, target):
        new_kpi = KPI(name, target)
        self.kpis.append(new_kpi)
        print(f"KPI '{name}' with a target of {target} added successfully!")

    def display_kpis(self):
        if not self.kpis:
            print("No KPIs added yet.")
        else:
            print("Current KPIs and their targets:")
            for i, kpi in enumerate(self.kpis, 1):
                print(f"{i}. KPI: {kpi.name} | Target: {kpi.target}")

def main():
    app = KPIApp()

    while True:
        print("\nOptions:")
        print("1. Add a KPI")
        print("2. Display KPIs")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            name = input("Enter KPI name: ")
            target = input("Enter KPI target: ")
            app.add_kpi(name, target)
        elif choice == '2':
            app.display_kpis()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()


ChatGPT said:
Here’s your KPI management app with a graphical user interface (GUI) using Tkinter. The app allows users to add KPIs and display them dynamically. 🎨🚀

Kpi Gui App

Answer in chat instead
This GUI-based KPI tracker replaces the console-based interaction with an intuitive interface using Tkinter. It includes:

✅ Input fields for KPI name and target
✅ Buttons to add and display KPIs
✅ A listbox to show the added KPIs
✅ Message popups for user feedback

Let me know if you’d like any enhancements! 🚀🎯


*************************

import tkinter as tk
from tkinter import messagebox

class KPI:
    def __init__(self, name, target):
        self.name = name
        self.target = target

class KPIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KPI Tracker")
        self.kpis = []
        
        # Labels
        self.label_name = tk.Label(root, text="KPI Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        
        self.label_target = tk.Label(root, text="Target:")
        self.label_target.grid(row=1, column=0, padx=10, pady=5)
        
        # Entry fields
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        self.entry_target = tk.Entry(root)
        self.entry_target.grid(row=1, column=1, padx=10, pady=5)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add KPI", command=self.add_kpi)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.display_button = tk.Button(root, text="Display KPIs", command=self.display_kpis)
        self.display_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Listbox to display KPIs
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def add_kpi(self):
        name = self.entry_name.get()
        target = self.entry_target.get()
        
        if name and target:
            new_kpi = KPI(name, target)
            self.kpis.append(new_kpi)
            messagebox.showinfo("Success", f"KPI '{name}' with target '{target}' added!")
            self.entry_name.delete(0, tk.END)
            self.entry_target.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both KPI name and target!")

    def display_kpis(self):
        self.listbox.delete(0, tk.END)
        if not self.kpis:
            self.listbox.insert(tk.END, "No KPIs added yet.")
        else:
            for i, kpi in enumerate(self.kpis, 1):
                self.listbox.insert(tk.END, f"{i}. {kpi.name} - Target: {kpi.target}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KPIApp(root)
    root.mainloop()
