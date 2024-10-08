class Cotxe:
    def __init__(self, model):
        self.model = model
    def __str__(self):
        return f"Soc un {self.model}"

    def conduir(self):
        print(f"Conduint un {self.model}")

a = Cotxe("seat")
print(a)
