"""
Проверка bash-скриптов на опасные команды перед выполнением.

🖊️ НАПИШИ САМ — заполни BLOCKED_PATTERNS, WARNING_PATTERNS и функцию validate_script()
Подсказки написаны в комментариях.
"""
import re
from dataclasses import dataclass, field

from src.core.logger import get_logger

logger = get_logger(__name__)


@dataclass
class ValidationResult:
    """Результат проверки скрипта."""

    is_safe: bool  # Можно ли выполнять?
    warnings: list[str] = field(default_factory=list)  # Предупреждения (не блокируют)
    blocked: list[str] = field(default_factory=list)  # Блокирующие находки


# Подсказка: каждый кортеж — (regex-паттерн, человекопонятное описание).
# Если regex найден в скрипте — скрипт ЗАБЛОКИРОВАН.
BLOCKED_PATTERNS: list[tuple[str, str]] = [
    # Твой код здесь. Примеры что блокировать:
    #
    # (r"\brm\s+-rf\s+/\s*$", "Recursive deletion of root filesystem"),
    # (r"\bmkfs\b", "Filesystem formatting"),
    # (r"\bdd\s+if=/dev/zero", "Disk zeroing"),
    # (r":\(\)\{.*:\|:&\s*\};:", "Fork bomb"),
    # (r"\b(systemctl|service)\s+(stop|disable|mask)\s+(sshd|ssh|NetworkManager)", "Disabling remote access"),
    # (r"\bchmod\s+-R\s+777\s+/", "World-writable root"),
    # (r"\bcurl\b.*\|\s*bash", "Piping remote script to bash"),
]

# Подсказка: предупреждения не блокируют, но показываются юзеру.
WARNING_PATTERNS: list[tuple[str, str]] = [
    # Твой код здесь. Примеры:
    #
    # (r"\b(reboot|shutdown|poweroff|init\s+[06])\b", "System reboot/shutdown"),
    # (r"\bapt-get\s+(remove|purge)\b", "Package removal"),
    # (r"\bsystemctl\s+restart\b", "Service restart"),
]


def validate_script(content: str) -> ValidationResult:
    """
    Проверяет содержимое скрипта на опасные команды.

    Подсказка:
    1. Создай два пустых списка: blocked = [] и warnings = []

    2. Пройдись по BLOCKED_PATTERNS:
       for pattern, description in BLOCKED_PATTERNS:
           if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
               blocked.append(description)

    3. Аналогично для WARNING_PATTERNS

    4. Если blocked не пустой:
       logger.warning("Script blocked! Dangerous commands: %s", blocked)

    5. Если warnings не пустой:
       logger.info("Script warnings: %s", warnings)

    6. return ValidationResult(
           is_safe=len(blocked) == 0,
           warnings=warnings,
           blocked=blocked,
       )
    """
    # Твой код здесь...
    pass
