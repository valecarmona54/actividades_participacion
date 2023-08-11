"""Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria."""

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, deposito):
        #deposito = float(input("Ingrese el deposito: "))
        self.balance += deposito
        

    def retiro(self, retiro):
        if self.balance - retiro >=0:
            self.balance -= retiro
        else:
            print("no tienes suficiente plata")        


    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
    
    def mostrar_detalles(self):
        print("detalles de la cuenta:")
        print("El numero de cuenta es: ",self.numero_cuenta)
        print("Los propietarios de la cuenta son:", self.propietarios)
        print("El balance es:" ,self.balance)

        
cuenta1 = CuentaBancaria("763542754", ("Paula y Pablo"), 50000)

deposito = float(input("Ingrese el monto a depositar: "))
cuenta1.depositar(deposito)


retiro = float(input("Ingrese el monto a retirar: "))
cuenta1.retiro(retiro)


cuenta1.aplicar_cuota_manejo()

cuenta1.mostrar_detalles()
