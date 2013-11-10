#encoding: utf-8

def opcoes():
    print "1 = Listar contatos existentes"
    print "2 = Adicionar contato"
    print "3 = Editar Contato"
    print "4 = Remover Contato"

    opt = raw_input()

def exibe_tela_inicial():

    print "Bem vindo a sua agenda de contatos."
    print "Por Favor escolha uma das ações abaixo:"

    opcoes()