-- dev etc
-- DROP TABLE IF EXISTS reading_cards;
-- DROP TABLE IF EXISTS spread_positions;
-- DROP TABLE IF EXISTS readings;
-- DROP TABLE IF EXISTS users;
-- DROP TABLE IF EXISTS cards;






-- Users table (simple for now)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL
);

-- Decks table
CREATE TABLE decks (
    id TEXT PRIMARY KEY,  -- e.g. 'rider_waite_classic'
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cards table (reference data, static per deck)
CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    name_short TEXT UNIQUE NOT NULL,  -- e.g. 'ar01'
    name TEXT NOT NULL,
    type TEXT,                        -- 'major', 'minor'
    suit TEXT,
    value INTEGER,
    position INTEGER,                 -- if you want to preserve card ordering
    meaning_up TEXT,
    meaning_rev TEXT,
    description TEXT,
    keywords TEXT[],                  -- Postgres array
    deck_id TEXT REFERENCES decks(id),
    image_url TEXT
);

-- Spread types
CREATE TABLE spreads (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,        -- e.g. 'past_present_future'
    description TEXT
);

-- Spread positions (e.g., 0: 'Past', 1: 'Present', etc.)
CREATE TABLE spread_positions (
    id SERIAL PRIMARY KEY,
    spread_id INTEGER REFERENCES spreads(id) ON DELETE CASCADE,
    position_index INTEGER NOT NULL,      -- 0, 1, 2, ...
    label TEXT NOT NULL,                  -- e.g. 'Past'
    UNIQUE(spread_id, position_index)
);

-- Readings
CREATE TABLE readings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    question TEXT,
    spread_id INTEGER REFERENCES spreads(id),
    deck_id TEXT REFERENCES decks(id),
    prompt_version TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    output_text TEXT,
    user_notes TEXT
);

-- Reading cards (record of cards drawn per reading)
CREATE TABLE reading_cards (
    id SERIAL PRIMARY KEY,
    reading_id INTEGER REFERENCES readings(id) ON DELETE CASCADE,
    position_index INTEGER NOT NULL,      -- index in spread
    card_id TEXT REFERENCES cards(name_short),
    is_reversed BOOLEAN DEFAULT FALSE,
    
    -- Snapshot of card at time of reading
    name TEXT,
    meaning_up TEXT,
    meaning_rev TEXT,
    keywords TEXT[],
    notes TEXT,

    UNIQUE(reading_id, position_index)
);

-- Optional tags for categorizing readings (future-proofing)
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    label TEXT UNIQUE NOT NULL
);

CREATE TABLE reading_tags (
    reading_id INTEGER REFERENCES readings(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (reading_id, tag_id)
);
