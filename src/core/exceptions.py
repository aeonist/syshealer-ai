"""Кастомные исключения SysHealer-AI."""


class SysHealerError(Exception):
    """Базовая ошибка. Все остальные наследуют от неё."""


class ConfigError(SysHealerError):
    """config.json повреждён или отсутствует."""


class AIProviderError(SysHealerError):
    """AI-провайдер не ответил, нет ключа, ответ не парсится."""


class ScriptValidationError(SysHealerError):
    """Скрипт содержит опасные команды."""


class ScriptExecutionError(SysHealerError):
    """Ошибка выполнения скрипта."""

    def __init__(self, message: str, exit_code: int = -1, stderr: str = ""):
        super().__init__(message)
        self.exit_code = exit_code
        self.stderr = stderr


class CircuitBreakerTripped(SysHealerError):
    """Превышен лимит попыток для инцидента."""
