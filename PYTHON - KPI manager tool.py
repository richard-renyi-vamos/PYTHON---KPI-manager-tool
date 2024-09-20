# Define a KPI class
class KPI:
    def __init__(self, name, target, unit=""):
        self.name = name
        self.target = target
        self.current_value = 0
        self.unit = unit

    def update(self, value):
        self.current_value += value
        self.check_status()

    def check_status(self):
        if self.current_value >= self.target:
            return "On Track"
        else:
            return "Below Target"

    def progress(self):
        progress_percentage = (self.current_value / self.target) * 100
        return f"{progress_percentage:.2f}%"

    def __str__(self):
        return (f"KPI: {self.name}\n"
                f"Target: {self.target} {self.unit}\n"
                f"Current: {self.current_value} {self.unit}\n"
                f"Status: {self.check_status()}\n"
                f"Progress: {self.progress()}\n")


# Define a KPI Manager class
class KPIManager:
    def __init__(self):
        self.kpis = []

    def add_kpi(self, name, target, unit=""):
        kpi = KPI(name, target, unit)
        self.kpis.append(kpi)

    def update_kpi(self, name, value):
        for kpi in self.kpis:
            if kpi.name == name:
                kpi.update(value)
                break

    def show_kpis(self):
        for kpi in self.kpis:
            print(kpi)


# Example usage
if __name__ == "__main__":
    # Create KPI manager
    kpi_manager = KPIManager()

    # Add some KPIs
    kpi_manager.add_kpi("Revenue", 1000000, "HUF")
    kpi_manager.add_kpi("Customer Satisfaction", 95, "%")
    kpi_manager.add_kpi("Website Traffic", 50000, "visits")

    # Update KPI progress
    kpi_manager.update_kpi("Revenue", 500000)
    kpi_manager.update_kpi("Customer Satisfaction", 90)
    kpi_manager.update_kpi("Website Traffic", 25000)

    # Show all KPIs and their status
    kpi_manager.show_kpis()
