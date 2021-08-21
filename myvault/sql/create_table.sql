CREATE TABLE IF NOT EXISTS local_vault (
  folder TEXT NOT NULL,
  name TEXT NOT NULL,
  secret TEXT NOT NULL,
  created_at TEXT NOT NULL,
  last_updated_at TEXT NOT NULL,
  UNIQUE(folder, name)
);
