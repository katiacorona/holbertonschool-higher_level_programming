-- Create the table unique_id on my MySQL server with attributes id and name.
CREATE TABLE IF NOT EXISTS unique_id (
        id   INT UNIQUE   DEFAULT 1,
        name VARCHAR(256)
);
