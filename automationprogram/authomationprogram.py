class Appliance:
    def __init__(self, name, power_usage):
        self.name = name
        self.power_usage = power_usage  # Power in watts
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"✅ {self.name} has been turned ON.")
        else:
            print(f"ℹ️ {self.name} is already ON.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"❌ {self.name} has been turned OFF.")
        else:
            print(f"ℹ️ {self.name} is already OFF.")

    def show_status(self):
        state = "ON" if self.is_on else "OFF"
        return f"{self.name:<20} | {state:^5} | {self.power_usage:>4} W"

class ApplianceManager:
    def __init__(self, power_limit=2000):
        self.appliances = []
        self.power_limit = power_limit

    def add_appliance(self, appliance):
        self.appliances.append(appliance)

    def turn_on(self, name):
        appliance = self.find_appliance(name)
        if appliance:
            if self.total_power() + appliance.power_usage <= self.power_limit:
                appliance.turn_on()
            else:
                print(f"⚠️ Power limit exceeded! Cannot turn on {name}.")
        else:
            print(f"❓ Appliance '{name}' not found.")

    def turn_off(self, name):
        appliance = self.find_appliance(name)
        if appliance:
            appliance.turn_off()
        else:
            print(f"❓ Appliance '{name}' not found.")

    def total_power(self):
        return sum(a.power_usage for a in self.appliances if a.is_on)

    def dashboard(self):
        print("\n📋 Appliance Status Dashboard")
        print("-" * 50)
        print(f"{'Appliance':<20} | {'State':^5} | {'Power'}")
        print("-" * 50)
        for a in self.appliances:
            print(a.show_status())
        print("-" * 50)
        print(f"🔋 Total Power Usage: {self.total_power()} W / {self.power_limit} W")

    def find_appliance(self, name):
        for a in self.appliances:
            if a.name.lower() == name.lower():
                return a
        return None


# Setup
manager = ApplianceManager(power_limit=2000)

# Add some appliances
manager.add_appliance(Appliance("Ceiling Fan", 75))
manager.add_appliance(Appliance("Air Conditioner", 1500))
manager.add_appliance(Appliance("Washing Machine", 500))
manager.add_appliance(Appliance("Heater", 1200))
manager.add_appliance(Appliance("Oven", 1800))

# Control appliances
manager.turn_on("Ceiling Fan")
manager.turn_on("Air Conditioner")
manager.turn_on("Washing Machine")  # This should exceed the power limit
manager.turn_off("Air Conditioner")
manager.turn_on("Washing Machine")  # Now it should work

# Show dashboard
manager.dashboard()
