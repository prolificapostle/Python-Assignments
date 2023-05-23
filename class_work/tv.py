class Tv:

    def __init__(self):
        self.power = False
        self.volume = 0

    def turn_on(self):
        if not self.power:
            self.power = True
            print("Tv is On")
        else:
            print("TV is already On")

    def turn_off(self):
        if self.power:
            self.power = False

    def increase_volume(self):
        if self.power:
            self.volume += 1

    def decrease_volume(self):
        self.volume -= 1


    def __str__(self):
        return f"{self.power}, {self.volume}"


samsung = Tv()

samsung.turn_on()
samsung.increase_volume()
samsung.increase_volume()
samsung.turn_on()
print(samsung)



