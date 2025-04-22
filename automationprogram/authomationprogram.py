class Appliance:
    def __init__(self, name, power_usage):
        self.name = name
        self.power_usage = power_usage  # Power consumption in watts
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} has been turned ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} has been turned OFF.")

    def show_status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"{self.name} is currently {state}. Power usage: {self.power_usage}W.")

# Let's create a few common home appliances
fan = Appliance("Ceiling Fan", 75)
air_conditioner = Appliance("Air Conditioner", 1500)
washing_machine = Appliance("Washing Machine", 500)

# Let's control these appliances
fan.turn_on()
air_conditioner.turn_off()
washing_machine.turn_on()

# Now let's check the current status of each appliance
print("\n--- Appliance Status ---")
fan.show_status()
air_conditioner.show_status()
washing_machine.show_status()
#total power consumption area
def calculate_total_power(appliances):
    total_power = sum(appliance.power_usage for appliance in appliances if appliance.is_on)
    print(f"\n🔋 Total Power Consumption of Running Appliances: {total_power}W")  
calculate_total_power(appliances)
