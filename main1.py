'''projeto para concluir tarefas de casa'''
class Tarefa:
    def __init__(self, descricao): 
        self.descricao = descricao
        self.feito = False
    

    def concluido(self):
        self.feito = True


    def __str__(self):
        return self.descricao + (' : concluido' if self.feito else '' ) 
        

casa = []
casa.append(Tarefa('passar roupa'))
casa.append(Tarefa('limpar xixi do bud'))


for c in casa:
    if c.descricao == 'limpar xixi do bud':  #.descricao:(foi colocado pq eh o parametro de 'passar roupa' e 'limpar xixi')
        c.concluido()

for k in casa:
    print(k)
