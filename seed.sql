TRUNCATE TABLE album;
TRUNCATE TABLE single;

ALTER SEQUENCE album_id_seq RESTART WITH 1;
ALTER SEQUENCE single_id_seq RESTART WITH 1;

INSERT INTO album(title, release_date, genre, record_label) VALUES
  ('Purple Rain', '1984-06-25', 'Pop, Rock, R&B', 'Warner Bros. Records'),
  ('Sign o'' the Times', '1987-03-30', 'Funk, R&B, Rock', 'Paisley Park Records'),
  ('1999', '1982-10-27', 'Funk, R&B, Pop', 'Warner Bros. Records');

INSERT INTO single(title, release_date, genre, record_label) VALUES
  ('When Doves Cry', '1984-05-16', 'Pop, Rock, R&B', 'Warner Bros. Records'),
  ('Kiss', '1986-02-05', 'Funk, R&B', 'Paisley Park Records'),
  ('Little Red Corvette', '1983-02-09', 'Pop, Rock, R&B', 'Warner Bros. Records');  