'''

-- Criação do banco de dados
CREATE DATABASE Escola;

-- Criação da tabela Alunos
CREATE TABLE Alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Criação da tabela Matriculas
CREATE TABLE Matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
    disciplina VARCHAR(100) NOT NULL,
    nota FLOAT,
    FOREIGN KEY (id_aluno) REFERENCES Alunos(id)
);
'''