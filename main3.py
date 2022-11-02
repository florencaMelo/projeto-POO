'''projeto aperfeiçoado'''

class Projeto:
    def __init__(self, nomeProjeto): 
        self.nomeProjeto = nomeProjeto
        self.lista = []
        
    
    def addTarefa(self, descricao):
        self.lista.append(Tarefa(descricao))
                
    
    def pendentes(self):
        return[c for c in self.lista if not c.feito]

        # for c in self.lista:
        #     if not c.feito:
        #         return c

  
    def __str__(self):
        return f'projeto {self.nomeProjeto} possui {len(self.pendentes())} tarefa(s) pendente(s)'


    def procurar(self, descricao):
        return[c for c in self.lista if c.descricao == descricao][0]

        # for c in self.lista:
        #     if c.descricao == descricao:
        #         return c


    def __iter__(self):
        self.lista.__iter__()
    



class Tarefa:
    def __init__(self, descricao): 
        self.descricao = descricao
        self.feito = False
    

    def concluido(self):
        self.feito = True


    def __str__(self):
        return self.descricao + (' : concluido' if self.feito else '' ) 
        


casa = Projeto('tarefas de casa')

casa.addTarefa('limpar chao')
casa.addTarefa('limpar xixi do bud')

casa.procurar('limpar xixi do bud').concluido()
print(casa)

for c in casa:
    print(c)
