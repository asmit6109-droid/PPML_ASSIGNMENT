class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)


# Creating an object
car1 = Car("Toyota", "Fortuner", "Black")
car2 = Car("BMW", "X5", "White")

car1.display()
car2.display()

