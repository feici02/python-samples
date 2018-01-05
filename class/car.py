#!/usr/bin/env python

class Car:
    def __init__(self, color='red', mileage=1000):
        self.color = color
        self.mileage = mileage
    
    def print(self):
        print('----------car info----------')
        print('color:   {}'.format(self.color))
        print('mileage: {}'.format(self.mileage))

def main():
    my_car = Car()
    my_car.print()

    my_car = Car('blue')
    my_car.print()

    my_car = Car(color='blue')
    my_car.print()

    my_car = Car(mileage=2000)
    my_car.print()


if __name__ == '__main__':
    main()