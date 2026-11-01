class dog():
    def sound(self):
        print("Bark")

class cat():
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

d=dog()
c=cat()

make_sound(d)
make_sound(c)