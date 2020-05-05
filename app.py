class Pilha():
  def __init__(self):
    self.elementos = list()
    self.capacidade = 10

  def push(self, valor):
    if self.estahCheia():
      return 'Pilha cheia'

    if type(valor) not in [int, str, float]:
      return 'erro'

    self.elementos.append(valor)
    return 'sucesso'

  def pop(self):
    if self.estahVazia():
      return 'Não existe nenhum elemento na pilha'

    return self.elementos.pop()

  def estahVazia(self):
    return len(self.elementos) == 0

  def estahCheia(self):
    return len(self.elementos) == self.capacidade

  def verificaTopo(self):
    if self.estahVazia():
      return 'Não existe topo'
    return self.elementos[-1]
