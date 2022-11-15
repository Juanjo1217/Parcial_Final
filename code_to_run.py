from Movie_Tikects import *

tr = theater()

usuario_1 = usuario("carlos", "VIP", 1)
ticket_1 = ticket(usuario_1.nombre, usuario_1.ticket, usuario_1.silla)
tr.registrar_usuario("carlos", 1)
print(ticket_1.nombre_usuario)