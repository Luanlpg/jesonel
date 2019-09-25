# crio classe
class NomeClasse():
    # (self é a propria classe)
    # inicio metodo construtor
    def __init__(self):
        self.atributo_1 = 'string'
        self.atributo_2 = 12345

    # crio metodo que mostra atributo_1
    def mostra_atributo_1(self):
        return self.atributo_1

    # crio metodo que mostra atributo_2
    def mostra_atributo_2(self):
        return self.atributo_2
# -----------fim da classe---------------



# instancio a classe em uma variável
objeto = NomeClasse()

# printo retorno de cada método
print(objeto.mostra_atributo_1())
print(objeto.mostra_atributo_2())

print(objeto.atributo_1)
print(objeto.atributo_2)
