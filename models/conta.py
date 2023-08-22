from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:

    codigo: int = 1001

    def __init__(self: object, Cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__Cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.00
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return