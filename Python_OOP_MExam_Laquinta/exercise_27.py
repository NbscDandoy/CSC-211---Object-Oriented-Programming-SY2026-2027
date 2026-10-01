class Device:
    def __init__(self, name):
        self.name = name


first = Device("D-01")
second = Device("D-02")
Device.room = "Lab 2"
first.room = "Repair Bench"
print(first.room)
print(second.room)
print(Device.room)