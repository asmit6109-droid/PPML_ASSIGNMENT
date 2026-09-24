class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    #Overloads '=='
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    # Overloads '*' for scalar multiplication: vector * scalar
    def __mul__(self, scalar):
        if isinstance(scalar,(int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented

    # Overloads '*' when object is on  the right: scalar * vector
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    #Readable representation 
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    #usage
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    v3 = v1 + v2
    print(v3)  # Output: Vector2D(4, 6)
    print(v1 == v2)  # Output: False
    print(v1 == Vector2D(1, 2))  # Output: True
    print(v1 * 3)  # Output: Vector2D(3, 6)
    print(3 * v1)  # Output: Vector2D(3, 6)