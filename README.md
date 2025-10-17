# CRUD com Mysql + Python + Streamlit

Este projeto é um exemplo prático de CRUD usando:
- Banco de dados **MYSQL**
- Conexão com o  **mysql.connector**
- Interface web com **Streamlit**


## Como executar

### 1. Clonar o nosso repositório


```bash
git clone https://github.com/pNogueira-DEV/Projeto-MYSQL
```



### 2. Instalar dependências
``` bash
pip install -r requirements.txt
```

### 3. configurar a variáveis de ambiente
crie um arquivo .env na raiz do seu projeto com:
```bash
DB_NAME=seu_DB
DB_USER= seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
```

### 4. Rodar aplicação
```bash
python -m streamlit run app.py
```

### 5 funcionalidades


- Inserir registros no db
- listar registros no db
- Atualizar registros no db
- Deletar registro no db
- Interface simples com Streamlit



