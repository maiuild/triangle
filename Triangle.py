class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    # Defineerin hüpotenuusi, valem on alus ruudus + kõrgus ruudus, millest on võetud ruutjuur
    def hypotenuse(self):
        return (self.base ** 2 + self.height ** 2) ** (1/2)

    # Defineerin kolmnurga ümbermõõdu. Valem on kõikide külgede summa
    def perimeter(self):
        return self.base + self.height + self.hypotenuse()

    # Defineerin kolmnurga pindala- alus * kõrgus ning jagatus kahega
    def area(self):
        return self.base * self.height * (1/2)
