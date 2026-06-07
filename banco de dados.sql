CREATE DATABASE IF NOT EXISTS crm CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE crm;

CREATE TABLE enderecos (
  id_endereco INT PRIMARY KEY AUTO_INCREMENT,
  cep VARCHAR(20),
  logradouro VARCHAR(255),
  numero VARCHAR(50),
  bairro VARCHAR(100),
  complemento VARCHAR(255),
  cidade VARCHAR(100),
  estado VARCHAR(50)
);

CREATE TABLE usuarios (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255),
  data_nascimento DATE,
  cpf VARCHAR(20),
  genero VARCHAR(20),
  telefone VARCHAR(50),
  email VARCHAR(255),
  senha VARCHAR(255),
  cargo VARCHAR(100),
  ativo TINYINT DEFAULT 1,
  id_endereco INT,
  FOREIGN KEY (id_endereco) REFERENCES enderecos(id_endereco) ON DELETE SET NULL
);

CREATE TABLE alunos (
  id_aluno INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255),
  data_nascimento DATE,
  cpf VARCHAR(20),
  genero VARCHAR(20),
  telefone VARCHAR(50),
  email VARCHAR(255),
  responsavel VARCHAR(255),
  status VARCHAR(50),
  id_endereco INT,
  FOREIGN KEY (id_endereco) REFERENCES enderecos(id_endereco) ON DELETE SET NULL
);

CREATE TABLE cursos (
  id_curso INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255),
  carga_horaria INT,
  valor DECIMAL(10,2),
  ativo TINYINT DEFAULT 1
);

CREATE TABLE disciplinas (
  id_disciplina INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255),
  id_curso INT,
  id_professor INT,
  carga_horaria INT,
  dia_semana VARCHAR(50),
  hora_inicio VARCHAR(20),
  hora_fim VARCHAR(20),
  ativa TINYINT DEFAULT 1,
  FOREIGN KEY (id_curso) REFERENCES cursos(id_curso) ON DELETE SET NULL,
  FOREIGN KEY (id_professor) REFERENCES usuarios(id_usuario) ON DELETE SET NULL
);

CREATE TABLE turmas (
  id_turma INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255),
  id_curso INT,
  id_disciplina INT,
  id_professor INT,
  horario VARCHAR(255),
  vagas INT,
  status VARCHAR(50),
  FOREIGN KEY (id_curso) REFERENCES cursos(id_curso) ON DELETE SET NULL,
  FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id_disciplina) ON DELETE SET NULL,
  FOREIGN KEY (id_professor) REFERENCES usuarios(id_usuario) ON DELETE SET NULL
);

CREATE TABLE matriculas (
  id_matricula INT PRIMARY KEY AUTO_INCREMENT,
  id_aluno INT,
  id_turma INT,
  data_matricula DATE,
  status VARCHAR(50),
  FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno) ON DELETE CASCADE,
  FOREIGN KEY (id_turma) REFERENCES turmas(id_turma) ON DELETE CASCADE
);

CREATE TABLE frequencias (
  id_frequencia INT PRIMARY KEY AUTO_INCREMENT,
  id_aluno INT,
  id_turma INT,
  data DATE,
  presente TINYINT,
  FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno) ON DELETE CASCADE,
  FOREIGN KEY (id_turma) REFERENCES turmas(id_turma) ON DELETE CASCADE
);

CREATE TABLE desempenho (
  id_desempenho INT PRIMARY KEY AUTO_INCREMENT,
  id_aluno INT,
  id_disciplina INT,
  valor DECIMAL(6,2),
  tipo VARCHAR(50),
  data DATE DEFAULT CURRENT_DATE,
  FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno) ON DELETE CASCADE,
  FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id_disciplina) ON DELETE CASCADE
);