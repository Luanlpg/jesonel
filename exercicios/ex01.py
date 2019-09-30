"""=============================================================================
Criar Classe Pessoa que receba os atributos(idade, altura e cor_dos_olhos) e
tenha metodos para retornar(return) estas informações
============================================================================="""


# Faça a classe aqui...
class Pessoa():
    def __init__(self, idade, altura, cor_dos_olhos):
        self.idade = idade
        self.altura = altura
        self.cor_dos_olhos = cor_dos_olhos

    def retorna_idade(self):
        return self.idade

    def retorna_altura(self):
        return self.altura

    def retorna_olhos(self):
        return self.cor_dos_olhos       
