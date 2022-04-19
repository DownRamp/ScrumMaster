-- Database: ScrumMaster

-- DROP DATABASE IF EXISTS "ScrumMaster";

CREATE DATABASE "ScrumMaster"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- 0 backlog, 1 current sprint, 2 active, 3 done --
CREATE TABLE Tickets (
	ticket_id serial PRIMARY KEY,
   	title VARCHAR ( 50 ) UNIQUE NOT NULL,
	label_val VARCHAR (50) NOT NULL,
   	description text NOT NULL,
   	docs int NOT NULL,
   	status int not null,
	priority text NOT NULL
);

CREATE TABLE Documents (
	doc_id serial PRIMARY KEY,
   	title VARCHAR ( 50 ) UNIQUE NOT NULL,
   	description text NOT NULL,
   	why text NOT NULL,
	repo_conn text NOT NULL,
	tests text NOT NULL,
	devs text NOT NULL,
	typ VARCHAR(50) NOT NULL
);

CREATE TABLE Updates (
   	date TIMESTAMP NOT NULL,
	ticket_id int not null,
	yesterday text not null,
	today text not null,
	blockers text
);

CREATE TABLE Connections (
   	repo1 VARCHAR(50) not null,
	repo2 VARCHAR(50) not null,
	description text not null
);
