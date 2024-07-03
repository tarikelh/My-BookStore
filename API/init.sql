-- Création de la table User
CREATE TABLE IF NOT EXISTS api_user (
    id SERIAL PRIMARY KEY,
    lastname VARCHAR(50),
    firstname VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    role VARCHAR(50) CHECK (role IN ('user', 'admin'))
);

-- Insertion de données par défaut dans la table User
INSERT INTO api_user (lastname, firstname, email, password, role) VALUES
('ADMIN', 'Admin', 'admin', 'bcrypt_sha256$$2b$12$fOH2o9z0SiszKWX67HFQ5eAhs0zK6XKllUTVV24/WVMbsV4H.obM2', 'admin'),
('DOE', 'John', 'john.doe@example.com', 'bcrypt_sha256$$2b$12$4x23LAr4kwHWlGKZin5dz.BbCR9MCM99WzGKDuu/D3LT/xAYpFh.m', 'user'),
('SMITH', 'Alice', 'alice.smith@example.com', 'bcrypt_sha256$$2b$12$q1Dv12yg/s.8MDugXDbOa.P5G8JqAblUj6JQZk3p5AH4K0Zy6qCwe', 'user');


-- Création de la table Product
CREATE TABLE IF NOT EXISTS api_product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(250),
    photo VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Insertion de données par défaut dans la table Product
INSERT INTO api_product (name, description, photo, price) VALUES
('Roman-Policier', 'Description of Product1', 'roman-policier.jpg', 16.99),
('Documentation-MySQL', 'Description of Product2', 'doc-mysql.jpg', 21.99),
('Manuel-Docker', 'Description of Product3', 'man-docker.jpg', 25.99);
