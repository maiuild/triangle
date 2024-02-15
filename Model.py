class Model:
    def __init__(self):
        self.base = 0  # Määran muutujatele algväärtused
        self.height = 0
        self.hypotenuse = 0
        self.perimeter = 0
        self.area = 0

    def calculate_triangle_properties(self, base, height):
        self.base = base
        self.height = height
        # Alus ja kõrgus sisestatakse kasutaja poolt, hüpotenuusi, ümbermõõdu ja pindala arvutatakse vastavalt inputile
        self.hypotenuse = (base**2 + height**2) ** (1/2)
        self.perimeter = base + height + self.hypotenuse
        self.area = (base * height) * (1/2)
        # Alust ja kõrgust ei ole vaja tagastada. Ainult need, millele omistatakse uus väärtus
        return self.hypotenuse, self.perimeter, self.area
