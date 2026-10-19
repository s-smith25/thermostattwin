class ThermostatTwin:
    def __init__(self, temperature=20, room="Living Room"):
        self.temperature = temperature
        self.room_name = room

    def set_temperature(self, new_temp):
        if new_temp > self.temperature:
            change = "rising"
        elif new_temp < self.temperature:
            change = "dropping"
        else:
            change = "unchanged"

        self.temperature = new_temp

        print(f"{self.room_name}: Temperature is {change} to {self.temperature}°C")

    def get_temperature(self):
        return self.temperature

    def location(self):
        return self.room_name

thermostat = ThermostatTwin(20, "Living Room")
thermostat.set_temperature(25)
thermostat.set_temperature(18)
thermostat.set_temperature(18)