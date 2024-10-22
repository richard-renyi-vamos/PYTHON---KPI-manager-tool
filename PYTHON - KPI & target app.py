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
