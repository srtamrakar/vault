UPDATE local_vault
SET secret = '{new_secret}',
    last_updated_at = '{timestamp}'
WHERE folder = '{folder}'
  AND name = '{name}';
