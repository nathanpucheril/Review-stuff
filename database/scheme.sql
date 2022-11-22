CREATE TABLE accounts ( -- TODO: Add Not Exists in other db
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      membership_plan TEXT NOT NULL
)

CREATE TABLE projects (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      account_id INTEGER NOT NULL,
      name TEXT NOT NULL,
      description TEXT NOT NULL,
  FOREIGN KEY(account_id) REFERENCES accounts(id)
)

CREATE TABLE  feedback (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  project_id INTEGER,
  type TEXT NOT NULL,
  blob TEXT NOT NULL, -- JSON BLOB TYPE
  FOREIGN KEY(project_id) REFERENCES projects(id)
);
