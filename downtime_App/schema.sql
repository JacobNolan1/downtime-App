DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS character;
DROP TABLE IF EXISTS activity;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS task_category;
DROP TABLE IF EXISTS earnings;
DROP TABLE IF EXISTS task_earnings;
DROP TABLE IF EXISTS campaign;
DROP TABLE IF EXISTS campaign_post;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE character(
  character_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  character_name VARCHAR(100) NOT NULL,
  character_str INTEGER NOT NULL,
  character_dex INTEGER NOT NULL,
  character_con INTEGER NOT NULL,
  character_int INTEGER NOT NULL,
  character_wis INTEGER NOT NULL,
  character_cha INTEGER NOT NULL,
  avaliable_downtime INTEGER NOT NULL,
  used_downtime INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE activity(
  activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
  character_id INTEGER NOT NULL,
  approved_status VARCHAR(100) NOT NULL,
  activity_status VARCHAR(100) NOT NULL,
  activity_type VARCHAR(100) NOT NULL,
  task_id INTEGER NOT NULL,
  FOREIGN KEY (character_id) REFERENCES character (character_id),
  FOREIGN KEY (task_id) REFERENCES task (task_id)
);

CREATE TABLE task(
  task_id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_desc VARCHAR(100) NOT NULL,
  task_summary TEXT NOT NULL,
  duration_days INTEGER NOT NULL
);

CREATE TABLE category(
  category_id INTEGER PRIMARY KEY AUTOINCREMENT,
  category_type VARCHAR(100) NOT NULL
);

CREATE TABLE task_category(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_id INTEGER NOT NULL,
  category_id INTEGER NOT NULL,
  FOREIGN KEY (task_id) REFERENCES task (task_id),
  FOREIGN KEY (category_id) REFERENCES category (category_id)
);

CREATE TABLE earnings(
  earnings_id INTEGER PRIMARY KEY AUTOINCREMENT,
  earning_desc TEXT NOT NULL
);

CREATE TABLE task_earnings(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_id INTEGER NOT NULL,
  earnings_id INTEGER NOT NULL,
  FOREIGN KEY (task_id) REFERENCES task (task_id),
  FOREIGN KEY (earnings_id) REFERENCES earnings (earning_id)    
);

CREATE TABLE campaign(
  campaign_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  campaign_name TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE campaign_post (
  post_id INTEGER PRIMARY KEY AUTOINCREMENT,
  campaign_id INTEGER NOT NULL,
  posted_at DATETIME NOT NULL,
  FOREIGN KEY (campaign_id) REFERENCES campaign (campaign_id)  
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);