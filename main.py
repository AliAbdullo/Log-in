class User:
  """User nomli class """
  def __init__(self, nickname, ism, familya, email):
    self.nick=nickname
    self.name= ism 
    self.surname = familya
    self.email = email

  def get_nick(self):
    """Foydalanuvchi Nicknameni qaytaradi"""
    return self.nick

  def get_name(self):
    """Foydalanuvchi ismini qaytaradi"""
    return self.name

  def get_surname(self):
    """Foydalanuvchi familyasini qaytaradi"""
    return self.surname

  def get_email(self):
    """Foydalanuvchi emailni qaytaradi"""
    return self.email

  def get_info(self):
    """Foydalanuvchi xaqida ma'lumot qaytaradi """
    return f"Foydalanuvchi:{self.nick}, ismi:{self.name} {self.surname}, email:{self.email}"


user1= User("Ali","Abdulloh","Abdug'aniyev","aliabdulloh@mail.ru") 
user2= User("Vali","Vali","Abdug'aniyev","valivali@mail.ru") 
user3= User("Sali","Sali","Abdug'aniyev","salisali@mail.ru")  
user4= User("Lali","Lali","Abdug'aniyev","Lalilali@mail.ru")  
user1= User("Ali","Abdulloh","Abdug'aniyev","aliabdulloh@mail.ru")  
user5= User("Ali","Abdulloh","Abdug'aniyev","aliabdulloh@mail.ru")  
user6= User("Ali","Abdulloh","Abdug'aniyev","aliabdulloh@mail.ru") 
  

print(user2.get_info())