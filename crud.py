from conexao import conectar

def inserir_aluno(nome_aluno, idade_aluno):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome, idade) VALUES (%s, %s)",
                (nome_aluno, idade_aluno)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar inserir aluno: {erro}")
        finally:
            cursor.close()
            conexao.cloese()

def listar_aluno():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM alunos ORDER BY ID"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao tentar exibir aluno: {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()

lista = listar_aluno()
for linha in lista:
    print(f" ID: {linha[0]} - NOME: {linha[1]} - IDADE: {linha[2]}")



def atualizar_alunos(id_aluno, nova_idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPTADE alunos SET idade = %s WHERE id = %s",
                (nova_idade, id_aluno)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar atualizar alunos: {erro}")
        finally:
            cursor.close()
            conexao.close()


            