from MyVault.src.helpers import FormattedEnum


class Prompt(FormattedEnum):
    CREATE_SQLITE_DB_CONFIRM = """
    Vault database does not exist.
    Create?
    Only 'yes' will be accepted to approve.
    """

    UPDATE_SECRET_CONFIRM = """
    A secret with the folder=`{folder}` and name=`{name}` already exists.
    Update its secret?
    Only 'yes' will be accepted to approve.
    """

    REMOVE_SECRET_CONFIRM = """
    Are you sure you want to remove the secret
    with the folder=`{folder}` and name=`{name}`?
    Only 'yes' will be accepted to approve.
    """

    ENCRYPTION_UPDATE_CONFIRM = """
    Are you sure you want to change the encryption configuration
    for `{db_path}`
    from `{config_path}`
    to `{new_path}`?
    Only 'yes' will be accepted to approve.
    """
