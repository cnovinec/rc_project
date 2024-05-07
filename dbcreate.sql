CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    email TEXT NOT NULL,
    hash TEXT NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    weight INTEGER NOT NULL
);

CREATE TABLE results (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    max_hang NUMERIC NOT NULL,
    weighted_finger_hang INTEGER NOT NULL,
    weighted_pullup INTEGER NOT NULL,
    core_strength NUMERIC NOT NULL,
    total_score INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE results_wheel (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    flexability INTEGER NOT NULL,
    dynamic_movment INTEGER NOT NULL,
    strength INTEGER NOT NULL,
    power INTEGER NOT NULL,
    endurance INTEGER NOT NULL,
    finger_strength INTEGER NOT NULL,
    balance INTEGER NOT NULL,
    technique INTEGER NOT NULL,
    total_score INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE rating_levels (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    score INTEGER NOT NULL,
    rating TEXT NOT NULL,
    level TEXT NOT NULL
);

INSERT INTO rating_levels (score, rating, level) VALUES(0, "18/below aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(1, "6a/19aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(2, "6a/19aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(3, "6b/21aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(4, "6b/21aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(5, "6c/23aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(6, "6c/23aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(7, "6c+/24aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(8, "6c+/24aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(9, "7a/25aus", "Beginer");
INSERT INTO rating_levels (score, rating, level) VALUES(10, "7a/25aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(11, "7a+/26aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(12, "7a+/26aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(13, "7b/26aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(14, "7b/26aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(15, "7b+/27aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(16, "7b+/27aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(17, "7c/28aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(18, "7c/28aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(19, "7c+/29aus", "Intermediate");
INSERT INTO rating_levels (score, rating, level) VALUES(20, "7c+/29aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(21, "8a/29aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(22, "8a/29aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(23, "8a+/30aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(24, "8a+/30aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(25, "8b/31aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(26, "8b/31aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(27, "8b+/32aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(28, "8b+/32aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(29, "8c/33aus", "Advance");
INSERT INTO rating_levels (score, rating, level) VALUES(30, "8c/33aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(31, "8c+/34aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(32, "8c+/34aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(33, "9a/35aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(34, "9a/35aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(35, "9a+/36aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(36, "9a+/36aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(37, "9b/37aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(38, "9b/37aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(39, "9b+/38aus", "Elite");
INSERT INTO rating_levels (score, rating, level) VALUES(40, "9C/39aus", "Elite");


