-- name: init#
DROP TABLE IF EXISTS items;

CREATE TABLE IF NOT EXISTS items (
  item_id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(100),
  PRIMARY KEY (item_id)
);
