-- This script creates a second table
create table if not exists second_table (
    id int primary key,
    name varchar(256),
    score int
);
insert into second_table values (1, 'John', 10);
insert into second_table values (2, 'Alex', 3);
insert into second_table values (3, 'Bob', 14);
insert into second_table values (4, 'George', 8);
