import sqlite3
import sys
import unittest
import uuid
from configparser import ConfigParser
from enum import Enum
from io import StringIO
from pathlib import Path

from MyVault import Vault
from MyVault.src.encryption import AESEncryption
from MyVault.src.statics import ExitCode

TEST_DIR = Path(__file__).parent


class TestConfigType(str, Enum):
    BAD_KEY = "bad_key"
    BAD_VALUE = "bad_value"
    GOOD = "good"


class TestConfig:

    SECTION = "cipher"

    def __init__(self, config_type: TestConfigType = TestConfigType.GOOD):
        self.path = TEST_DIR / f"{uuid.uuid4()}.cfg"
        self.config = ConfigParser()
        self.values = {
            "key": "replace-me",
            "salt": "replace-me",
            "iterations": "10",
            "clipboard_ttl": "3",
        }
        self.create_file(config_type=config_type)

    def create_file(self, config_type: TestConfigType):
        if config_type == TestConfigType.BAD_KEY:
            self.config[TestConfigType.BAD_KEY] = self.values

        elif config_type == TestConfigType.BAD_VALUE:
            self.values["iterations"] = "Ten"
            self.config[self.SECTION] = self.values

        else:
            # i.e. config_type == TestConfigType.GOOD
            self.config[self.SECTION] = self.values

        with open(file=self.path, mode="w") as config_file:
            self.config.write(fp=config_file)

    def __del__(self):
        self.path.unlink()


class TestDatabase:
    def __init__(self):
        self.path = TEST_DIR / f"{uuid.uuid4()}.sqlite3"
        self.create_file()

    def create_file(self):
        conn = sqlite3.connect(self.path)
        conn.close()

    def __del__(self):
        self.path.unlink()


class TestEncryptionConfig(unittest.TestCase):
    def test_good(self):
        sys.stdout = StringIO()
        db = TestDatabase()
        config = TestConfig(config_type=TestConfigType.GOOD)
        vault = Vault(db_path=db.path, config_path=config.path)
        sys.stdout = sys.__stdout__
        self.assertEqual(int(config.config["cipher"]["clipboard_ttl"]), vault.clipboard_ttl)

    def test_bad_key(self):
        sys.stdout = StringIO()
        db = TestDatabase()
        config = TestConfig(config_type=TestConfigType.BAD_KEY)
        with self.assertRaises(SystemExit) as err:
            _ = Vault(db_path=db.path, config_path=config.path)
        sys.stdout = sys.__stdout__
        self.assertEqual(err.exception.code, ExitCode.INVALID_KEY)

    def test_bad_value(self):
        sys.stdout = StringIO()
        db = TestDatabase()
        config = TestConfig(config_type=TestConfigType.BAD_VALUE)
        with self.assertRaises(SystemExit) as err:
            _ = Vault(db_path=db.path, config_path=config.path)
        sys.stdout = sys.__stdout__
        self.assertEqual(err.exception.code, ExitCode.INVALID_VALUE)


class TestVault(unittest.TestCase):

    DB = TestDatabase()
    CONFIG = TestConfig(config_type=TestConfigType.GOOD)
    CIPHER = AESEncryption(
        key=str(CONFIG.config["cipher"]["key"]),
        salt=str(CONFIG.config["cipher"]["salt"]),
        iterations=int(CONFIG.config["cipher"]["iterations"]),
    )

    FOLDER = "test_folder"
    NAME = "first"
    SECRET = "first_password"

    NONE_EXISTENT_FOLDER = "none_existent_folder"
    NONE_EXISTENT_NAME = "none_existent_name"

    def test_insert(self):
        sys.stdout = StringIO()
        with Vault(db_path=self.DB.path, config_path=self.CONFIG.path) as vault:
            vault.upsert(folder=self.FOLDER, name=self.NAME, secret=self.SECRET)
            secret = vault.copy(folder=self.FOLDER, name=self.NAME, get=True)
            self.assertEqual(self.CIPHER.decrypt(ciphertext=secret), self.SECRET)
        sys.stdout = sys.__stdout__

    def test_none_existent_secret(self):
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit) as err:
            vault = Vault(db_path=self.DB.path, config_path=self.CONFIG.path)
            _ = vault.copy(folder=self.NONE_EXISTENT_FOLDER, name=self.NONE_EXISTENT_NAME, get=True)
        self.assertEqual(err.exception.code, ExitCode.SECRET_NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
