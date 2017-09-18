# Stack

Implementação de uma pilha que contém as operações pop, push e min feitas em O(1)
Segue abaixo breve explicação sobre o porquê de todas as operações serem realizadas em O(1)

## Push

Em uma pilha todos os elementos são adicionados sempre em uma extremidade, e removido da outra. Por conta disso não há necessidade de ficar percorrendo vários elementos para adicionar ou remover um elemento na pilha. Para fazer isso, implementei uma lista simplesmente encadeada utilizando uma classe Node que armezana o valor e a referência para o elemento imediatamente abaixo na pilha. Com isso, ao adicionar um valor no topo da pilha, basta que esse novo elemento tenha o valor do topo antigo como próximo e a pilha agora tenha como novo topo, o elemento associado. O(1)

## Pop

Para remover elemento da pilha, basta que o topo passe a apontar para o próximo do Nó removido. Não precisei desalocar porque a partir do momento que não há mais referências para um objeto, o garbage collector do CPython desaloca esse elemento pra mim, impedindo de gastar memória atoa. O(1)

## Min

Bom, esse é o método mais difícil de ser implementado na complexidade O(1) pois se fosse para comparar os elementos da pilha para achar o menor, a opção mais eficiente seria utilizar algoritmos de ordenação, como o quickSort e depois pegar o primeiro elemento, mas isso não ocorre em O(1), pois o tempo varia com o tamanho da entrada.
Para chegar na complexidade O(1) é preciso gastar mais memória e armazenar numa pilha temporária *MinStack* o histórico dos menores valores, e ir atualizando conforme eles forem saindo da pilha, ou entrando valores menores que o menor atual.