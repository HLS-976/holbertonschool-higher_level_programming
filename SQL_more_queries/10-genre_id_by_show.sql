-- This scripts lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows JOIN tv_shows_genres ON tv_shows_genres.show_id = tv_shows.id  ORDER BY tv_shows.title AND tv_shows_genres.genre_id;
