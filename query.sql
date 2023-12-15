-- 1.Вивести кількість манги для кожного жанру
SELECT g.genre, COUNT(mg.manga_id) AS manga_count
FROM genre g
JOIN manga_genre mg ON g.genre_id = mg.genre_id
GROUP BY g.genre;

-- 2.Вивести кількість манги за кожним статусом
SELECT s.status, COUNT(m.manga_id) AS manga_count
FROM status s
JOIN manga m ON s.status_id = m.status_id
GROUP BY s.status;

-- 3.Вивести залежність кількості розділів від статусу манги
SELECT s.status, AVG(m.chapters) AS avg_chapters
FROM manga m
JOIN status s ON m.status_id = s.status_id
GROUP BY s.status;