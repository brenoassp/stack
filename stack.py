# -*- coding: utf-8 -*-

## Não preciso desalocar o que vai saindo da pilha pois o
## garbage collector do CPython conta o número de referências
## para o objeto, ou seja, quando eu apontar o topo pro
## proximo, não terá mais nada apontando pro nó removido
## e ele será desalocado automaticamente

class Node:
	def __init__(self, value):
		self.prox = None
		self.value = value

# Pilha auxiliar para guardar o histórico de menores valores da pilha
class MinStack:
	def __init__(self):
		self.top = None

	def pop(self):
		value = self.top.value
		self.top = self.top.prox
		return value

	def push(self,value):
		new_node = Node(value)
		new_node.prox = self.top
		self.top = new_node

	def is_empty(self):
		return self.top == None

class Stack:
	def __init__(self):
		self.min_stack = MinStack()
		self.top = None

	def pop(self):
		if self.min_stack.is_empty():
			raise Exception('The Stack is Empty!')
		else:
			if self.min() == self.top.value:
				self.min_stack.pop()
			value = self.top.value
			self.top = self.top.prox
			return value

	def push(self, value):
		if self.is_empty():
			self.min_stack.push(value)
			new_node = Node(value)
			self.top = new_node
		else:
			if value < self.min():
				# Se o valor a ser inserido é menor do que o menor valor atual da pilha, é inserido na pilha auxiliar MinStack
				# Dessa forma, mantém um histórico de menores valores para quando o menor for removido, ainda ser possível
				# saber qual será o novo menor
				self.min_stack.push(value)
			new_node = Node(value)
			new_node.prox = self.top
			self.top = new_node

	# Retorna o valor mínimo da pilha com complexidade O(1), 
	# pois é só acessar diretamente o topo da pilha MinStack
	def min(self):
		if not self.is_empty():
			return self.min_stack.top.value
		else:
			raise Exception('The Stack is Empty!')

	# Verifica se a pilha está vazia, basta verificar se há elemento 
	# na MinStack já que o primeiro elemento sempre é inserido lá também
	def is_empty(self):
		return self.min_stack.is_empty()

def main():
	stack = Stack()
	op = -1
	while op != 4:
		print('1 - Adicionar elemento')
		print('2 - Remover elemento')
		print('3 - Retornar menor elemento')
		print('4 - Sair')
		print('Selecione uma opcao')
		op = int(input(""))

		if op == 0:
			break
		elif op == 1:
			value = int(input("Forneca o numero para ser adicionado na pilha "))
			stack.push(value)
		elif op == 2:
			stack.pop()
		elif op == 3:
			print('Menor elemento da pilha = ',stack.min())

if __name__ == '__main__':
	main()