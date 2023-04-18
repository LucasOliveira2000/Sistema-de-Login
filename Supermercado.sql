CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome_de_usuario VARCHAR(255) NOT NULL,
    senha CHAR(10) NOT NULL,
    email VARCHAR(255) NOT NULL,
    data_de_nascimento DATE NOT NULL
);

SELECT * FROM usuarios;



