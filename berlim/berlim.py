#Berlim Portões
from time import sleep
from os import system
import json

class Portao:       

    def __init__(self, id):
        self.aberto = 'nao'
        self.id = id
        self.name = 'Portão ' + str(self.id )

    '''
        objeto portao serve para checar se o portão seguinte está aberto
        antes de tentar abrir o portão inicial, obedecendo a regra
        de intertravamento
    '''
    def abrir(self, portao):
        if portao.aberto == 'nao':
            if self.aberto == 'nao':                
                self.envia_comando()
                self.tempo_acionamento('abrindo...')
                self.aberto = 'sim' 
                print(self.name, 'aberto')                            

    def fechar(self):
        if self.aberto == 'sim':
            self.envia_comando()
            self.tempo_acionamento('fechando...')
            self.aberto = 'nao'
            print(self.name, 'fechado')                         
    
    def tempo_acionamento(self, status):
        print(self.name, status)       
        for i in range(10):
            system('echo|set /p="."')
            #print('.', end='')  
            #sleep(0.1)              
        print()

    def envia_comando(self):
        print()
        print('comando enviado...')

def invert_io(key, value):
    with open('io.json', 'r+') as json_io:
        data = json.load(json_io)
        data[key] = value
        json_io.seek(0)
        json_io.write(json.dumps(data))
        json_io.truncate()

def iniciar():
    
    io = ''    
    portao_loop1 = ''
    portao_loop2 = ''
    
    while True:

        with open('io.json', 'r') as json_io:
            io = json.load(json_io)

        if io['acionamento_p1'] == 'sim':
            portao1.abrir(portao2)
            portao1.fechar()
            portao_loop1 = portao2
            portao_loop2 = portao1
            invert_io('acionamento_p1', 'nao')
        elif io['acionamento_p2'] == 'sim':
            portao2.abrir(portao1)
            portao2.fechar()
            portao_loop1 = portao1
            portao_loop2 = portao2
            invert_io('acionamento_p2', 'nao')
        
        if io['loop'] == 'ativo':
            if portao_loop1.aberto == 'nao' and portao_loop1.aberto == 'nao':
                print()
                print('## PORTÃO ACIONADO PELO LAÇO ##')
                portao_loop1.abrir(portao_loop2)
                portao_loop1.fechar()
                invert_io('loop', 'inativo')
        sleep(2)

portao1 = Portao(1)
portao2 = Portao(2)

iniciar()