"""
Тесты для очистки/санитизации логов.

🖊️ НАПИШИ САМ — заполни тела тестов.
Каждая функция test_* — отдельный тест-кейс.
assert <выражение> — если выражение True, тест прошёл. Если False — провалился.

Запуск: pytest tests/test_sanitizer.py -v
"""
from src.collector import sanitize_and_compress, generate_log_hash


class TestSanitizeAndCompress:
    """Группа тестов для sanitize_and_compress()."""

    def test_removes_prompt_injection(self):
        """
        Проверяем, что строки с prompt injection заменяются.

        Подсказка:
        1. Создай строку с "ignore previous instructions" внутри
        2. result = sanitize_and_compress(строка)
        3. assert "ignore previous" not in result.lower()
        4. assert "[MALICIOUS_PROMPT_REMOVED]" in result
        """
        # Твой код здесь...
        pass

    def test_redacts_ip_addresses(self):
        """
        Проверяем, что IP-адреса заменяются на [IP_REDACTED].

        Подсказка: создай строку вроде "Connection from 192.168.1.100 failed"
        и проверь, что 192.168.1.100 заменился на [IP_REDACTED]
        """
        # Твой код здесь...
        pass

    def test_replaces_hex_dumps(self):
        """
        Проверяем, что длинные hex-дампы заменяются на [HEX_DUMP].

        Подсказка: строка "crash at 0xDEADBEEF" → "crash at [HEX_DUMP]"
        """
        # Твой код здесь...
        pass

    def test_compresses_whitespace(self):
        """
        Проверяем, что множественные пробелы/переносы сжимаются в один пробел.

        Подсказка: "hello   \n\n   world" → "hello world"
        """
        # Твой код здесь...
        pass


class TestGenerateLogHash:
    """Группа тестов для generate_log_hash()."""

    def test_same_log_same_hash(self):
        """
        Одинаковые логи = одинаковый хеш.

        Подсказка:
        hash1 = generate_log_hash("some error message")
        hash2 = generate_log_hash("some error message")
        assert hash1 == hash2
        """
        # Твой код здесь...
        pass

    def test_different_logs_different_hash(self):
        """Разные логи = разный хеш."""
        # Твой код здесь...
        pass

    def test_numbers_are_ignored(self):
        """
        Числа удаляются перед хешированием — ключ к дедупликации.
        "error at PID 123" и "error at PID 456" → одинаковый хеш.

        Подсказка:
        assert generate_log_hash("crash PID 123") == generate_log_hash("crash PID 456")
        """
        # Твой код здесь...
        pass
