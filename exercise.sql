CREATE TABLE IF NOT EXISTS person (
	id INTEGER PRIMARY KEY,	
	name TEXT,
	age INTEGER,
	sex TEXT
);

INSERT INTO person(name,age,sex) VALUES
("foo",20,"f");

CREATE TABLE IF NOT EXISTS pet (
	id INTEGER PRIMARY KEY,
	name TEXT,
	breed TEXT,
	age INTEGER
);

INSERT INTO pet(name,breed,age) VALUES
("romeo","parakeet",3);

PRAGMA foreign_keys = ON;

CREATE TABLE person_pet (
	person_id INTEGER,
	pet_id INTEGER,
	FOREIGN KEY (person_id) REFERENCES person (id),
	FOREIGN KEY (pet_id) REFERENCES pet (id)
);

INSERT INTO person_pet VALUES (1,1);
