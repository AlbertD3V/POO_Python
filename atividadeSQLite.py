import sqlite3


class DataBase():
    def __init__(self,info_DB) -> None:
        self.info_DB = info_DB
        self.conn = None
        self.cursor = None

    def conecta_db(self):
        self.conn = sqlite3.connect(self.info_DB)
        self.cursor = self.conn.cursor()
        return "conectado"
    
    def desconect_db(self):
        self.conn.close()
        return "Desconectado"
    
    def criando_tabela(self):
        self.conecta_db()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS slientes(
                            id INTEGER PRIMARY KEY,
                            nome VACHAR(50) NOT NULL,
                            cpf INTEGER NOT NULL); """)
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS produto(
                            produtos_id INTEGER PRIMARY KEY,
                            nome_produto VACHAR(50),
                            valor FLOAT,
                            cod_produto INTEGER NOT NULL,
                            FOREIGN KEY(cod_produto) REFERENCES clientes(id));""")
        self.conn.commit(); print("banco de dados criado") 

    def insert_dadso_clients(self,nome,cpf):
        self.conecta_db()
        self.cursor.execute(f"""
                            INSERT INTO clientes(nome,cpf)
                            VALUES(?,?)""",(nome,cpf))
        self.conn.commit()
        self.desconect_db()

    def update_dados_clients(self,novo_nome,novo_cpf,id_cliente):
        self.conecta_db()
        self.cursor.execure(f"UPDATE clietes SET nome = ?,cpf = ? WHERE id = ?",(novo_nome,novo_cpf,id_cliente))
        self.conn.commit()
        self.desconect_db()
        return("Informações alteradas com sucesso!")
    
    def delete_user(self,id):
        self.conecta_db()
        self.cursor.execute(f"DELETE FROM clientes WHERE id = ?",(id))
        self.conn.commit()
        self.desconect_db()
        return(f"Usuario deletado com sucesso!")
    
    def select_all_clients(self):
        self.conecta_db()
        return self.cursor.execute("SELECT FROM * clientes;").fetchall()
    
    def select_for_id(self,id):
        self.conecta_db()
        return self.cursor.execute(f"SELECT * FROM clientes WHERE id = ?",[id]).fetchall()
    
    def alterar_nomeTabela(self):
        self.conecta_db()
        self.cursor.execute(""" ALTER TABLE slientes RENAME TO clientes """)
        self.conn.commit()
        self.desconect_db()







