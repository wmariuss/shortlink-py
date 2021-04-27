-- Creation of short table
CREATE TABLE short (
url_id SERIAL PRIMARY KEY,
long_url VARCHAR(255),
short_url VARCHAR(10)
);
