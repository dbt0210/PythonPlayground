class Beer:
    _vols = {"Krombacher": 4.8, "Veltins": 5.0, "Bitburger": 4.2, "Pißwasser": 6.0}

    def __init__(self, brand: str="Krombacher", amount: "Amount in Liters"=1 / 3, vol: "Percent alcohol"=0.0):
        self.brand = brand
        self.plopped = False
        self.amount = amount
        if brand in Beer._vols:
            self.vol = Beer._vols[brand]
        else:
            self.vol = vol

    def __str__(self):
        return "A " + self.brand + " with " + str(self.vol) + "% vol."

    def sip(self):
        if self.plopped:
            return self.amount - 0.01 if self.amount - 0.01 > 0 else 0
        else:
            raise PermissionError("Beer is not plopped")

    def plopp(self):
        self.plopped = True


b = Beer("Lager", 1, 10.0)
print(b)
b.plopp()
b.sip()