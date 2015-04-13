class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3D(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3D(x, y, z)

    def __mul__(self, other):
        # Multiplikation mit Skalar
        if type(other) in (int, float, complex):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        # Kreuzprodukt
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)

    def __str__(self):
        return "Vector3D({0}, {1}, {2})".format(self.x, self.y, self.z)


a = Vector3D(0, 5, 0)
a += Vector3D(5, 0, 1)
print(a)
a -= Vector3D(3, 3, 3)
print(a)
print(Vector3D(0, 0, 1) * 3)
