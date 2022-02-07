CREATE TABLE ethereum_events(
    id  SERIAL PRIMARY KEY,
    args  JSON,
    event  VARCHAR(128),
    log_index  INTEGER,
    transaction_index  INTEGER,
    transaction_hash  VARCHAR(68),
    address  VARCHAR(68),
    block_hash  VARCHAR(68),
    block_number  INTEGER,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ethereum_blocks(
    id SERIAL PRIMARY KEY,
    block_height INTEGER,
    mined_at timestamp,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pageview_counts (
    pagename VARCHAR(50) NOT NULL,
    pageviewcount INT NOT NULL,
    datetime TIMESTAMP NOT NULL
);

