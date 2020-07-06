# cadastramento_processos

Esse projeto realiza o cadastramento de processos através do upload de planilhas. Deve ser realizado o upload de uma planilha no formato CSV contendo pasta, comarca e uf dos processos. Um processo por linha.


## Instalação

Considerando que o projeto faz uso de banco de dados para o armazenamento de planilhas e processos, devem ser realizadas preparações para tal.
Devem ser realizados os seguintes comandos no terminal linux, no diretório raiz do projeto:

```
>> python3 manage.py makemigrations cadastro_processo 
>> python3 manage.py makemigrations colecao_processos
>> python3 manage.py migrate

```

## Endpoints

O projeto possui 3 endpoints que são acessíveis via navegador:

* processos/: Lista em formato JSON os processos cadastrados no sistema (via upload de planilhas). 
* planilhas/: Lista em formato JSON as planilhas enviadas ao sistema por upload de arquivos.
* planilhas/upload: Exibe uma página HTML onde o usuário indica seu nome, cliente e o arquivo csv referente a planilha para upload. Realizado o upload, o usuário é redirecionado para /processos/.

## Exemplos

Acessando o sistema antes de realizar o upload de nenhuma planilha:

processos/
```json
{
    "Processos": []
}

```

planilhas/
```json
{
    "Planilhas": []
}

```

Realizando o upload da planilha "processos.csv", com o nome "joao" e cliente "monte" no endpoint planilhas/upload. O usuário então é redirecionado novamente para /processos, que irá visualizar o seguinte output:

```json
{
    "Processos": [
        {"uf": "SP", "pasta": "92381", "comarca": "Sao Paulo"},
        {"uf": "CE", "pasta": "21421", "comarca": "Ceara"},
        {"uf": "PE", "pasta": "34234", "comarca": "Recife"},
        {"uf": "PE", "pasta": "43983", "comarca": "Garanhuns"},
        {"uf": "PR", "pasta": "43232", "comarca": "Londrina"},
        {"uf": "RJ", "pasta": "32344", "comarca": "Rio de Janeiro"}
    ]
}

```

Ao acessar planilhas/ , o usuário poderá visualizar informações sobre a planilha inserida no sistema.

```json
{
    "Planilhas": [
        {"cliente": "Monte", "arquivo": "processos.csv", "nome": "Joao"}
    ]
}

