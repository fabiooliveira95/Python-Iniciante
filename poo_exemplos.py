from decimal import Decimal


class Ball:
    def __init__(self, color="unknown", circumference=0, material="unknown"):
        self.color = color
        self.circumference = circumference
        self.material = material

    def change_color(self):
        to_replace = input(f"Você quer mudar a cor atual {self.color}? [y/n]: ").lower()
        if to_replace == 'y':
            new_color = input("Nova cor: ")
            self.color = new_color
        else:
            print(f"OK, a cor permanece {self.color}")

    def show_color(self):
        print(f"\nA cor atual é {self.color}")


class Square:
    def __init__(self, size=30, greeting=20):
        self.size = size
        self.greeting = greeting

    def __str__(self):
        size_names = ['small', 'medium', 'large', 'extra large']
        greeting_names = ['Hello', 'Hi', 'Welcome', 'Greetings']
        try:
            return f"{greeting_names[self.greeting % len(greeting_names)]} of {size_names[self.size % len(size_names)]}"
        except IndexError:
            return "Invalid size or greeting index"


class Rectangula:
    def __init__(self, length=50, width=30):
        self.length = length
        self.width = width
        self._kind = 'numeric'  # Default type, can be changed

    def __str__(self):
        return f"Rectangle: {self.length} x {self.width}"

    def validate(self, value):
        if self._kind == 'bigint':
            return isinstance(value, int)
        elif self._kind == 'varchar':
            return isinstance(value, str)
        elif self._kind == 'numeric':
            try:
                Decimal(value)
                return True
            except:
                return False
        return False


class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = int(age)
        self.weight = float(weight)
        self.height = float(height)
        self._date = []

    def date(self):
        return self._date


class Car:
    def __init__(self, wheels=0, steering_wheel=0, airbag=0):
        self.wheels = wheels
        self.steering_wheel = steering_wheel
        self.airbag = airbag

    def __str__(self):
        return f"Car: Rodas={self.wheels}, Volante={self.steering_wheel}, Airbag={self.airbag}"


class Television:
    def __init__(self, channel=10, volume=30):
        self._channel = channel
        self._volume = volume

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, number):
        if str(number).isdigit():
            num = int(number)
            if 0 < num <= 130:
                self._channel = num
            else:
                print("Canal inválido")
        else:
            print("O canal deve ser um número")

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, number):
        if str(number).isdigit():
            num = int(number)
            if 0 <= num <= 100:
                self._volume = num
            else:
                print("Nível de volume inválido")
        else:
            print("O volume deve ser um número")

    def __str__(self):
        return f"Canal: {self.channel}\nVolume: {self.volume}"


class FuelPump:
    def __init__(self, fuel_type, liter_value, amount_of_fuel):
        self.fuel_type = fuel_type
        self.liter_value = liter_value
        self.amount_of_fuel = amount_of_fuel

    def supply_by_value(self, amount_paid):
        amount_of_liters = amount_paid / self.liter_value
        self.amount_of_fuel += amount_of_liters
        return amount_of_liters

    def supply_by_liter(self, amount_of_liters):
        amount_paid = amount_of_liters * self.liter_value
        self.amount_of_fuel += amount_of_liters
        return amount_paid

    def change_value(self, new_value):
        self.liter_value = new_value

    def change_fuel(self, new_quantity):
        self.amount_of_fuel = new_quantity


def main():
    ball = Ball("azul", 5, "metal")
    while True:
        ball.show_color()
        ball.change_color()

        continue_game = input("Continue? [y/n]: ").lower()
        if continue_game == 'n':
            ball.show_color()
            break


if __name__ == "__main__":
    main()
