from enum import Enum


class FormattedEnum(str, Enum):
    def formatted(self, **kwargs) -> str:
        return self.value.format(**kwargs)
