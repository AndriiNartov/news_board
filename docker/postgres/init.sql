CREATE USER news_board_user WITH PASSWORD 'devpass';

CREATE DATABASE news_board_db;

GRANT ALL PRIVILEGES ON DATABASE news_board_db TO news_board_user;
