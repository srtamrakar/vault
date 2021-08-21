UPDATE local_vault
SET secret = ?,
    last_updated_at = ?
WHERE folder = ?
  AND name = ?;
