# Welcome to Marvel World

Por meio desta API, podemos acessar informações referentes ao mundo Marvel. Através do endpoint Characters Marvel.

## Bibliotecas Utilizadas

Primeiramente, vamos realizar a instalação das bibliotecas utilizadas no projeto, para isso basta inserir o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

As configurações e versões dessas bibliotecas utilizadas encontram-se no documento ``` requirements.txt```.


## Iniciando a API

Para iniciar a APi via terminal usaremos o comando  ``` python main.py ``` que irá ler nosso arquivo principal.

Ao realizar essa leitura, podemos ver que foi gerado na pasta raiz do projeto um arquivo csv com os dados requisitados um arquivos index.html, ao abrimos o index.html no navegador teremos os nossos Characters puxados da API da Marvel.
## Testes no Postman

Podemos testar nosso endpoint pelo Postman, segue URL utilizada para realizar a requisição:

```https://gateway.marvel.com/v1/public/characters?apikey=af42d135bf129d0ef2e79e2a3abb2e92&ts={{today}}&hash={{hash}}```

Lembrando que é necessário colocar os parâmetros ```apikey, ts e hash``` para conseguirmos acessar a requisição e o método HTTP será o GET.

## Autoria

Anne Carvalho 
## License

[MIT](https://choosealicense.com/licenses/mit/)


