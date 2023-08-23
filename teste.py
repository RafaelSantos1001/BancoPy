from models.cliente import Cliente
from models.conta import Conta


felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-01', '10/01/1994')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '234.567.890-02', '20/02/1994')

# print(felicity)
# print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

# print(contaf)
# print(contaa)


