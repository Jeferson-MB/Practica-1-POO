from User import User
from Lugar import Lugar
from Foto import Foto
from Roles import Rol

Lugar1 = Lugar("Zoologico","Zona 13","12340987")
Lugar2 = Lugar("Tikal Futura","Zona 11",'45902365')
Lugar3 = Lugar("Palaciona Nacional",'Zona 1',"89345610")
Lugar4 = Lugar('Oaklan Mall','zona 10',"20035719")

Foto1 = Foto('imagenes/fotos/usuario.png','png','1.2')
Foto2 = Foto('imagenes/fotos/perfil.jpg','jpg','2.3')
Foto3 = Foto('imagenes/fotos/wallpaper.jpeg',"jpeg","200")
Foto4 = Foto("imagenes/fotos/imagen1.jpg",'jpg','90')

User1 = User(f"Jeferson","Barrera",[Foto1,Foto2], [Rol.Ad, Rol.Ing])
User1.setLugaresFreceuntes(Lugar1)
User1.setLugaresFreceuntes(Lugar2)
print(User1)

User2 = User(f"Alexander","Lima",[Foto1,Foto4], [Rol.Ing, Rol.Es])
User2.setLugaresFreceuntes(Lugar3)
User2.setLugaresFreceuntes(Lugar1)
print(User2)

User3 = User(f"Hector","Godoy",[Foto3,Foto1], [Rol.Ma, Rol.Ad])
User3.setLugaresFreceuntes(Lugar3)
User3.setLugaresFreceuntes(Lugar4)
print(User3)

User4 = User(f"Graciela","Michiely",[Foto2,Foto4], [Rol.Co, Rol.Rep])
User4.setLugaresFreceuntes(Lugar4)
User4.setLugaresFreceuntes(Lugar2)
print(User4)