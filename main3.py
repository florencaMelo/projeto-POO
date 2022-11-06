'''projeto aperfeiçoado'''
from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nomeProjeto): 
        self.nomeProjeto = nomeProjeto
        self.lista = []
        
    
    def addTarefa(self, descricao, vencimento=None):
        self.lista.append(Tarefa(descricao, vencimento))
        self.vencimento = vencimento
                
    
    def pendentes(self):
        return[c for c in self.lista if not c.feito]
        """ for c in self.lista:
            if not c.feito:
                return c """
  
    def __str__(self):
        return f'projeto {self.nomeProjeto} possui {len(self.pendentes())} tarefa(s) pendente(s)'


    def procurar(self, descricao):
        return[c for c in self.lista if c.descricao == descricao][0]
        """ for c in self.lista:
            if c.descricao == descricao:
                return c """


    



class Tarefa:
    def __init__(self, descricao, vencimento=None): 
        self.descricao = descricao
        self.feito = False
        self.vencimento = vencimento
    

    def concluido(self):
        self.feito = True


    def __str__(self):
        status = []
        if self.vencimento:
            if self.vencimento <= datetime.now():
                status.append('vencido')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'faltam {dias} dias para vencer')
        elif self.feito:
            status.append('tarefa concluida')

        return f'{self.descricao} = {status}'



        
        


casa = Projeto('tarefas de casa')

casa.addTarefa('limpar chao', datetime.now() + timedelta(days=1, minutes=4))
casa.addTarefa('limpar xixi do bud')
casa.addTarefa('limpar cozinha', datetime.now())

casa.procurar('limpar xixi do bud').concluido()
print(casa)

for c in casa.lista:
    print(c)
 
