# Etapa 1 - Programa 

O programa que printa a variável de ambiente do SO a cada 20s foi escrito em Python:

```python
import os
import time

timeout = 20.0
 
db_usr = os.getenv('USERNAME')
 
db_pass = os.getenv('PASSWORD')

def twenty_seconds_log():
    print(db_pass)    

while True:
    twenty_seconds_log()
    time.sleep(timeout)
```

As variáveis [USERNAME, PASSWORD] serão incluídas nos recursos dos deployments como Secrets.

# Etapa 2 - Criação do container e updload da imagem Docker

Criei o container utilizando o Docker, o arquivo Dockfile ficou desse jeito:

```Dockfile
FROM python:latest

COPY main.py /

CMD ["python","-u","main.py"]
``` 
Utilizei também o Docker Hub como container registry


```python
import os
import time

timeout = 20.0
 
db_usr = os.getenv('USERNAME')
 
db_pass = os.getenv('PASSWORD')

def twenty_seconds_log():
    print(db_pass)    

while True:
    twenty_seconds_log()
    time.sleep(timeout)
```

# Saída

O programa gera o arquivo "output.txt", com o conteúdo no formato esperado do desafio.
