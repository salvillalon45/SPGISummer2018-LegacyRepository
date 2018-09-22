-- Salvador Villalon
-- SPGI SUMMER 2018
-- --------------------------------------------------------
-- This query joins two tables:
-- wp_users and wp_posts_1 so that we can get the five values listed
-- the select statement
SELECT post.ID, wp_users.user_nicename, post.post_date, post.post_title, post.post_content 
FROM wp_posts post
INNER JOIN wp_users ON post.post_author = wp_users.ID;

-- SELECT post.ID
-- FROM wp_posts_1 post
-- INNER JOIN wp_users ON post.post_author = wp_users.ID;