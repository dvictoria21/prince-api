DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS single;

CREATE TABLE album (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  release_date DATE,
  genre VARCHAR(255),
  record_label VARCHAR(255)
);

CREATE TABLE single (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  release_date DATE,
  genre VARCHAR(255),
  record_label VARCHAR(255)
);