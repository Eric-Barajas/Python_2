SELECT * FROM books_schema.favorites;

DELETE FROM favorites WHERE id = 5;
-- Query: Remove the first user of the 3rd book's favorites

INSERT INTO favorites (book_id, user_id) VALUES (2, 5);
-- Query: Have the 5th user favorite the 2nd book
