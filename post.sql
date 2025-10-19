
--@block
CREATE Table Posts(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    content TEXT,
    category VARCHAR(255),
    tags VARCHAR(255),
    createdAt TIMESTAMP,
    updatedAt TIMESTAMP
);

--@block
INSERT INTO posts (title, content, category, tags)
VALUES(
    'First blog',
    'Excited to write this blog',
    'blogs',
    'technology'
);

--@block
DELETE FROM posts WHERE id = 2;

--@block
SELECT * FROM posts;