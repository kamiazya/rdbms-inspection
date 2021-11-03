-- name: insert_item<!
INSERT INTO items (name)
  VALUES (:name);


-- name: update_item<!
UPDATE items
  SET name = :name
  WHERE item_id = :item_id;
