DROP TABLE IF EXISTS seasons;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS time;

CREATE TABLE teams (
  name varchar(255) NOT NULL,
  PRIMARY KEY (name));

CREATE TABLE time (
  year int(10) NOT NULL AUTO_INCREMENT,
  CONSTRAINT time
    PRIMARY KEY (year));

CREATE TABLE seasons (
  team_name             varchar(255) NOT NULL,
  year                  int(10) NOT NULL,
  total_wins            int(10),
  total_losses          int(10),
  total_overtime_losses int(10),
  percentage_wins       float,
  goals_for             int(10),
  goals_against         int(10),
  goals_difference      int(10));

ALTER TABLE seasons ADD CONSTRAINT FKseasons73808 FOREIGN KEY (team_name) REFERENCES teams (name);
ALTER TABLE seasons ADD CONSTRAINT FKseasons342066 FOREIGN KEY (year) REFERENCES time (year);