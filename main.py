class User:
  def __init__(self, ism, familiyasi, oismi, traqami, email):
    self.ism=ism
    self.lastname=familiyasi
    self.otasiningIsmi=oismi
    self.telefonNumber=traqami
    self.emanzil=email
    
  def get_name(self):
    """Ismni qaytarib beradi"""
    return self.ism

  def get_info(self):
    """Foydalanuvchi malumotlari """
    print( f"Foydalanuvchi:{self.ism}, ismi:{self.lastname} {self.otasiningIsmi}, telefon raqami: {self.telefonNumber}")



user1 = User("Vali","Saliy","Ani", +998902067510, "zizizizi")  
people= User("Ali",  "Abdulloh", "Abdumutalogli", +998901695979, "abdjf")
print(people.get_name())
print(user1.get_info())

  