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
CREATE TABLE tickets (
	ticket_id serial PRIMARY KEY,
   	title VARCHAR ( 50 ) UNIQUE NOT NULL,
	label_val VARCHAR (50) NOT NULL,
   	description text NOT NULL,
   	docs int NOT NULL,
   	status int not null,
	prty text NOT NULL
);

CREATE TABLE documents(
	doc_id serial PRIMARY KEY,
   	title VARCHAR ( 50 ) UNIQUE NOT NULL,
   	description text NOT NULL,
   	why text NOT NULL,
	repo_conn text NOT NULL,
	tests text NOT NULL,
	devs text NOT NULL,
	typ VARCHAR(50) NOT NULL
);

CREATE TABLE hire(
	hire_id serial PRIMARY KEY,
	date TIMESTAMP NOT NULL,
	reason text not null,
	team text not null,
	pay_range text
);

CREATE TABLE updates(
	ticket_id serial PRIMARY KEY,
	today text NOT NULL,
	yesterday text not null,
	today_work text not null,
	blockers text
);

CREATE TABLE rolodex (
	full_name text not null PRIMARY KEY,
	title text not null,
	email text not null
	);
