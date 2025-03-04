-- That script creates a table in a database
create table if not exists first_table (
    id serial primary key,
    name varchar(255) not null
);
