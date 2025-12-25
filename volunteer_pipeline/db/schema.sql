CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dob TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS member_skills (
    member_id INTEGER,
    skill_id INTEGER
);

CREATE TABLE IF NOT EXISTS persona (
    member_id INTEGER,
    persona TEXT,
    confidence REAL
);
