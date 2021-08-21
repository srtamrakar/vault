from MyVault.src.helpers import FormattedEnum


class Message(FormattedEnum):
    DB_CREATED = """
    Vault database is created `{db_path}`.
    """

    DB_CONN_CLOSED = """
    Connection to the vault database is closed.
    """

    DB_REQUIRED_WARNING = """
    Cannot continue without creating a vault database.
    """

    CONFIG_KEY_WARNING = """
    Config file is missing either a section: `cipher`,
    or the key(s): `KEY`, `SALT`, `ITERATIONS`, `CLIPBOARD_TTL`.
    """

    CONFIG_VALUE_WARNING = """
    Values of `KEY`, `SALT`, `ITERATIONS`, and `CLIPBOARD_TTL`
    must be of type `string`, `string`, `integer` and `integer` respectively.
    """

    SECRET_INSERTED = """
    Secret with folder=`{folder}`, name=`{name}` is inserted.
    """

    SECRET_UPDATED = """
    Secret with folder=`{folder}`, name=`{name}` is updated.
    """

    UPDATE_ABORTED = """
    Update secret is aborted.
    """

    SECRET_DELETED = """
    Secret with folder=`{folder}`, name=`{name}`, if exists, is deleted.
    """

    REMOVE_ABORTED = """
    Delete secret is aborted.
    """

    SECRET_NOT_FOUND = """
    Secret not found with folder=`{folder}`, name=`{name}`.
    """

    SECRET_COPIED = """
    Secret with folder=`{folder}`, name=`{name}` is copied to clipboard for {ttl} seconds.
    Press Ctrl+C if done early.
    """

    INVALID_CONFIG_WARNING = """
    Could not decrypt the secret.
    Please confirm that the config file is correctly upsert and try again.
    """

    ENCRYPTION_UPDATED = """
    A copy of vault database with old encryption config is saved to
    `{db_path}` for backup.

    Encryption is updated using new config file.
    """

    ENCRYPTION_ABORTED = """
    Encryption using new config file is aborted.
    """

    FOLDERS_NAMES_PRINT = """
    Folder/Names in the vault database:
    """
