import unittest
from app import Pilha


class PilhaTest(unittest.TestCase):
  def test_deve_retornar_estahVazia_True(self):
    p = Pilha()
    result = p.estahVazia()
    self.assertEqual(result, True)

  def test_deve_retornar_estahVazia_False_(self):
    p = Pilha()
    p.push('A')
    result = p.estahVazia()
    self.assertEqual(result, False)

  def test_deve_retornar_sucesso_quando_push_string(self):
    p = Pilha()
    result = p.push('A')
    self.assertEqual(result, 'sucesso')

  def test_deve_retornar_sucesso_quando_push_int(self):
    p = Pilha()
    result = p.push(3)
    self.assertEqual(result, 'sucesso')

  def test_deve_retornar_sucesso_quando_push_float(self):
    p = Pilha()
    result = p.push(3.5)
    self.assertEqual(result, 'sucesso')

  def test_deve_retornar_erro_quando_push_boolean(self):
    p = Pilha()
    result = p.push(True)
    self.assertEqual(result, 'erro')

  def test_deve_retornar_cheio_quando_push(self):
    p = Pilha()
    p.push('A')
    p.push('B')
    p.push('C')
    p.push('D')
    p.push('E')
    p.push('F')
    p.push('G')
    p.push('H')
    p.push('I')
    p.push('J')
    result = p.push('K')
    self.assertEqual(result, 'Pilha cheia')

  def test_deve_retornar_elemento_quando_pop(self):
    p = Pilha()
    elemento = 'A'
    p.push(elemento)
    result = p.pop()
    self.assertEqual(result, elemento)

  def test_deve_retornar_erro_quando_pop(self):
    p = Pilha()
    result = p.pop()
    self.assertEqual(result, 'Não existe nenhum elemento na pilha')

  def test_deve_retornar_erro_quando_pop_mais_vezes_que_elementos(self):
    p = Pilha()
    p.push('A')
    p.push('B')
    p.pop()
    p.pop()
    result = p.pop()
    self.assertEqual(result, 'Não existe nenhum elemento na pilha')

  def test_deve_retornar_true_quando_estahcheia(self):
    p = Pilha()
    p.push('A')
    p.push('B')
    p.push('C')
    p.push('D')
    p.push('E')
    p.push('F')
    p.push('G')
    p.push('H')
    p.push('I')
    p.push('J')
    result = p.estahCheia()
    self.assertEqual(result, True)

  def test_deve_retornar_false_quando_nao_estahcheia(self):
    p = Pilha()
    p.push('A')
    result = p.estahCheia()
    self.assertEqual(result, False)

  def test_deve_retornar_false_quando_verifica_topo(self):
    p = Pilha()
    result = p.verificaTopo()
    self.assertEqual(result, 'Não existe topo')

  def test_deve_retornar_A_quando_verifica_topo(self):
    p = Pilha()
    p.push('A')
    result = p.verificaTopo()
    self.assertEqual(result, 'A')

  def test_deve_retornar_B_quando_verifica_topo(self):
    p = Pilha()
    p.push('A')
    p.push('B')
    result = p.verificaTopo()
    self.assertEqual(result, 'B')

  def test_deve_retornar_C_quando_verifica_topo(self):
    p = Pilha()
    p.push('A')
    p.push('B')
    p.push('C')
    p.push('D')
    p.pop()
    result = p.verificaTopo()
    self.assertEqual(result, 'C')


if __name__ == '__main__':
  unittest.main()
