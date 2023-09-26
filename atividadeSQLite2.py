from atividadeSQLite import DataBase


Atletas = DataBase("info.db")

Atletas.criando_tabela()

Atletas.insert_dadso_clients("Albert Dias", 3350751895)
