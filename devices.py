

class Lamp:
    """
    Simulates a smart lamp.
    """
    def __init__(self, location: str):
        self.location = location.lower()
        self.is_on = False
        print(f"Lamp created for {self.location}.")

    def turn_on(self) -> str:
        """Turns the lamp on."""
        if not self.is_on:
            self.is_on = True
            return f"Lamp in {self.location} is now ON."
        return f"Lamp in {self.location} is already ON."

    def turn_off(self) -> str:
        """Turns the lamp off."""
        if self.is_on:
            self.is_on = False
            return f"Lamp in {self.location} is now OFF."
        return f"Lamp in {self.location} is already OFF."

    def get_status(self) -> str:
        """Returns the current status of the lamp."""
        status = "ON" if self.is_on else "OFF"
        return f"Lamp in {self.location} is currently {status}."

    def get_location(self) -> str:
        return self.location

class ACUnit:
    """
    Simulates a smart AC unit.
    """
    def __init__(self, location: str):
        self.location = location.lower()
        self.is_on = False
        self.temperature = 24  # Default temperature
        print(f"AC Unit created for {self.location}.")

    def turn_on(self) -> str:
        """Turns the AC unit on."""
        if not self.is_on:
            self.is_on = True
            return f"AC unit in {self.location} is now ON. Temperature set to {self.temperature}°C."
        return f"AC unit in {self.location} is already ON."

    def turn_off(self) -> str:
        """Turns the AC unit off."""
        if self.is_on:
            self.is_on = False
            return f"AC unit in {self.location} is now OFF."
        return f"AC unit in {self.location} is already OFF."

    def set_temperature(self, temperature: int) -> str:
        """Sets the temperature of the AC unit."""
        if not self.is_on:
            return f"AC unit in {self.location} is OFF. Please turn it on first to set temperature."
        if 18 <= temperature <= 30: # Example valid range
            self.temperature = temperature
            return f"AC unit in {self.location} temperature set to {self.temperature}°C."
        return f"Temperature {temperature}°C is out of valid range (18-30°C) for AC unit in {self.location}."

    def get_status(self) -> str:
        """Returns the current status of the AC unit."""
        status = "ON" if self.is_on else "OFF"
        temp_info = f", current temperature: {self.temperature}°C" if self.is_on else ""
        return f"AC unit in {self.location} is currently {status}{temp_info}."

    def get_temperature(self) -> str:
        """Returns the current set temperature of the AC unit."""
        if self.is_on:
            return f"AC unit in {self.location} temperature is currently set to {self.temperature}°C."
        return f"AC unit in {self.location} is OFF, no temperature set."

    def get_location(self) -> str:
        return self.location

class Television:
    """
    Simulates a smart television.
    """
    def __init__(self, location: str):
        self.location = location.lower()
        self.is_on = False
        self.channel = 1
        self.is_muted = False
        print(f"Television created for {self.location}.")

    def turn_on(self) -> str:
        """Turns the television on."""
        if not self.is_on:
            self.is_on = True
            return f"Television in {self.location} is now ON. Currently on channel {self.channel}."
        return f"Television in {self.location} is already ON."

    def turn_off(self) -> str:
        """Turns the television off."""
        if self.is_on:
            self.is_on = False
            return f"Television in {self.location} is now OFF."
        return f"Television in {self.location} is already OFF."

    def change_channel(self, channel: int) -> str:
        """Changes the television channel."""
        if not self.is_on:
            return f"Television in {self.location} is OFF. Please turn it on first to change channel."
        if 1 <= channel <= 100: # Example valid range for channels
            self.channel = channel
            return f"Television in {self.location} channel changed to {self.channel}."
        return f"Channel {channel} is out of valid range (1-100) for television in {self.location}."

    def mute(self) -> str:
        """Mutes the television."""
        if not self.is_on:
            return f"Television in {self.location} is OFF. Please turn it on first to mute."
        if not self.is_muted:
            self.is_muted = True
            return f"Television in {self.location} is now MUTED."
        return f"Television in {self.location} is already MUTED."

    def unmute(self) -> str:
        """Unmutes the television."""
        if not self.is_on:
            return f"Television in {self.location} is OFF. Please turn it on first to unmute."
        if self.is_muted:
            self.is_muted = False
            return f"Television in {self.location} is now UNMUTED."
        return f"Television in {self.location} is already UNMUTED."

    def get_status(self) -> str:
        """Returns the current status of the television."""
        status = "ON" if self.is_on else "OFF"
        channel_info = f", current channel: {self.channel}" if self.is_on else ""
        mute_info = ", (Muted)" if self.is_muted and self.is_on else ""
        return f"Television in {self.location} is currently {status}{channel_info}{mute_info}."

    def get_channel(self) -> str:
        """Returns the current channel of the television."""
        if self.is_on:
            return f"Television in {self.location} is currently on channel {self.channel}."
        return f"Television in {self.location} is OFF, no channel displayed."

    def get_location(self) -> str:
        return self.location

# A central dictionary to store all device instances
# This will be populated when the main application starts
# Example usage (for testing purposes, run this part in a separate test file or in main.py temporarily):
# if __name__ == "__main__":
#    kitchen_lamp = Lamp("Kitchen")
#     kitchen_lamp.turn_on()
#     print(kitchen_lamp.get_status())
#     kitchen_lamp.turn_off()
#     print(kitchen_lamp.get_status())

#     room1_ac = ACUnit("Room 1")
#     room1_ac.turn_on()
#     room1_ac.set_temperature(20)
#     print(room1_ac.get_status())
#     room1_ac.set_temperature(10) # Out of range
#     room1_ac.turn_off()
#     print(room1_ac.get_status())

#     living_room_tv = Television("Living Room")
#     living_room_tv.turn_on()
#     living_room_tv.change_channel(5)
#     living_room_tv.mute()
#     print(living_room_tv.get_status())
#     living_room_tv.unmute()
#     print(living_room_tv.get_status())
#     living_room_tv.turn_off()