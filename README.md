# TP2 - Parte 1 Questão 2: tradução do inglês para francês

API desenvolvida com FastAPI e Transformers, utilizando o modelo Helsinki-NLP/opus-mt-en-fr

Recebe texto em inglês por JSON e devolve a tradução para o francês.

## Organização

- main.py inicializa a API e define o endpoint
- models.py define os modelos de entrada e saída
- tradução.py carrega o modelo e traduz por parágrafos
- teste_traducao.py realiza teste local de tradução
- requirements.txt estabelece as dependências e versões
- .gitignore exclui os arquivos do versionamento

O modelo é carregado uma vez por processo e reutilizado nas requisições

## Como executar no Windows com Git Bash
Abra o terminal na pasta do projeto.
Crie o ambiente virtual no caminho "C:/Python Projects/venvs/tp2-fr"
Ative o ambiente
Instale as dependências
Inicie o servidor: python -m uvicorn main:app --port 8001 --reload
Acesso a documentação
Na primeira execução, é necessário acesso à internet para baixar o modelo.
A aplicação utiliza CPU.

## Endpoint
POST /traduzir

Exemplo de entrada: "texto": "Hello, how are you?"}

A resposta contém texto_original e texto_traduzido

Para separar parágrafos no JSON, utilize \n\n dentro da string

## Textos maiores e limitações
O texto é dividido pelas linhas em branco entre parágrafos.
Cada parágrafo é traduzido separadamente e os resultados são 
reunidos na ordem original.

Nos testes, foi recuperado uma frase omitida quando o texto longo 
foi passado de uma vez.

Ainda podem ocorrer erros e omissões de tradução. A separação também 
reduz o contexto compartilhado entre parágrafos.

Cada tradução gera até 500 novos tokens.
Esse limite não garante que toda saída estará completa.

