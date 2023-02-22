CREATE TABLE places
(
	city VARCHAR(255) NOT NULL,
	county VARCHAR(255) NOT NULL,
	country VARCHAR(255) NOT NULL,
	PRIMARY KEY (city)
) COMMENT='This is the places table';


CREATE TABLE people
(
	people_id INTEGER NOT NULL AUTO_INCREMENT,
	given_name VARCHAR(255) NOT NULL,
	family_name VARCHAR(255) NOT NULL,
	date_of_birth DATE NOT NULL,
	place_of_birth VARCHAR(255) NOT NULL,
	PRIMARY KEY (people_id),
	CONSTRAINT fk_places FOREIGN KEY (place_of_birth)  
	  REFERENCES places(city)  
) COMMENT='This is the people table';
