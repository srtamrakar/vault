# MyVault

A simple, offline vault to store secrets e.g. your password.

* SQLite database is used for storage.
* Each secret is AES-256 encrypted using an SHA-256 hash generated from a key*, salt*, and iterations*.
* The decrypted secret can only be copied to the clipboard*.
* Secrets are never displayed, logged, or uploaded anywhere.

*\*: Should be [configured](#configuration).*

## Installation with pip

Requirement: Python 3.7+

### Source: PyPi
```bash
$ pip3 install MyVault
```

## Configuration

Configuration for the encryption is provided as a *cfg* file.

Example: [cipher_example.cfg](cipher_example.cfg)
```buildoutcfg
[cipher]
key = replace-me
salt = replace-me
iterations = 100000
clipboard_ttl = 15
```

Notes:
* `key`: Key, a hash of which is used for encryption.
* `salt`: Salt for hashing.
* `iterations`: Iterations for hashing.
* `clipboard_ttl`: Seconds to retain copied secret in the clipboard.

## Usage

### Commands

#### General

* See available commands:
    ```bash
    $ myvault --help
    Usage: myvault [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      add     Add a secret (will be prompted) to the vault.
      copy    Copy the decrypted secret from the vault to the clipboard.
      remove  Delete either a secret by its folder and name.
      list    List all the folders and names of secrets.
      update  Update encryption configuration for the vault.
    ```

* Help for a specific command: `$ myvault <command> --help`

  Example:
    ```bash
    $ myvault add --help
    Usage: myvault add [OPTIONS] NAME [FOLDER]

      Add a secret (will be prompted) to the vault.

    Options:
      --config FILE  Path to the encryption config file.  [required]
      --db FILE      Path to the vault database.  [required]
      --help         Show this message and exit
    ```

#### Add a secret

If the vault database does not exist, it will be created. After the following command is run, you will see a prompt to enter the secret.
```bash
$ myvault add --db=<path_to_sqlite3_file> --config=<path_to_config_file> instagram social-media
```

#### List secrets

All the folders and names of secrets will be listed.
```bash
$ myvault list --db=<path_to_sqlite3_file> --config=<path_to_config_file>
```

#### Copy a secret

Copy the decrypted secret from the vault to the clipboard.
```bash
$ myvault copy --db=<path_to_sqlite3_file> --config=<path_to_config_file> instagram social-media
```

#### Remove a secret

Delete a secret by its folder and name.
```bash
$ myvault remove --db=<path_to_sqlite3_file> --config=<path_to_config_file> instagram social-media
```

#### Update encryption configuration

Update encryption configuration for the vault.
```bash
$ myvault update --db=<path_to_sqlite3_file> --config=<path_to_config_file> <path_to_new_config_file>
```

:warning: Make sure to pass the correct path to `--config` once the encryption config is updated. Otherwise, `copy` could either return an empty string `""` or exit with the status `INVALID_CONFIG_ERROR`.

### Recommendations

1. Use an external drive to store the vault database, as well as the config file so that the vault is **isolated and mobile**.
1. Create aliases so that the **CLI commands are shortened**.
   1. Add the following lines in *shell profile*:
        ```text
        MYVAULT_DB="<absolute_path_to_db>"
        MYVAULT_CONFIG="<absolute_path_to_config>"
        alias vault-ad="myvault add --db=$MYVAULT_DB --config=$MYVAULT_CONFIG"
        alias vault-cp="myvault copy --db=$MYVAULT_DB --config=$MYVAULT_CONFIG"
        alias vault-ls="myvault list --db=$MYVAULT_DB --config=$MYVAULT_CONFIG"
        alias vault-up="myvault update --db=$MYVAULT_DB --config=$MYVAULT_CONFIG"
        alias vault-rm="myvault remove --db=$MYVAULT_DB --config=$MYVAULT_CONFIG"
        ```
   1. Shortened cli commands:
       ```bash
       $ vault-ad insta social_media
       $ vault-cp insta social_media
       $ vault-ls
       $ vault-rm insta social_media
       $ vault-up /Volumes/external/new_config.cfg
       ```

## Author

**&copy; 2021, [Samyak Tamrakar](https://www.linkedin.com/in/srtamrakar/)**.
