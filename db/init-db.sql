  CREATE TABLE usuario (
  id serial PRIMARY KEY,
   usuario VARCHAR(60), 
   password VARCHAR(60), 
   email VARCHAR(60));
  
  CREATE TABLE video_conversion (
  id VARCHAR(40) PRIMARY KEY,
  video BYTEA,
  video_name VARCHAR(40),
  original_format VARCHAR(40),
  upload_date TIMESTAMP,
  video_converted BYTEA,
  conversion_format VARCHAR(40),
  conversion_date TIMESTAMP,
  state VARCHAR(40),
  usuario_id integer REFERENCES usuario(id));
