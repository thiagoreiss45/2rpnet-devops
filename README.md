# Execução do programa

Antes de executar o programa, o nome do arquivo de entrada deve ser inserido no lugar de "insira_aqui_o_arquivo", linha 6.

Isso pode ser feito de duas formas:
* abre o "test.txt" que esteja no diretório atual
```
f = open("test.txt")
```

* abre o "test.txt" especificamento o diretório
```
f = open("C:/Python33/test.txt")
```
Para executar: 
```
python parentheses-challenge.py
```

# Algoritmo

A função recebe a expressão e percorre todos os caracteres da string, caso ele encontre ```'('``` ```var``` é incrementada, caso encontre ```')'``` ```var``` é decrementada. 
Uma expressão válida, é uma expressão onde ```var``` seja igual a 0, ou seja, cada ```'('``` anula um ```')'```, porém:

>se ```var < 0``` significa que algum parênteses foi fechado sem ser aberto e o programa retorna 'incorrect'.

>se ```var > 0``` significa que algum parêtenses foi aberto sem ser fechado e o programa retorna 'incorrect'.

```python
def isExpressionValid(exp):
    var = 0
    for c in exp:
        if var < 0:
            return 'incorrect'
        elif c == '(':
            var += 1
        elif c == ')':
            var -= 1
    if var == 0:
        return 'correct'
    else:
        return 'incorrect'
```

# Saída

O programa gera o arquivo "output.txt", com o conteúdo no formato esperado do desafio.