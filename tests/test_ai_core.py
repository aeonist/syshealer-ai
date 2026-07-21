"""
Тесты для парсинга ответов AI.

🖊️ НАПИШИ САМ — заполни тела тестов.

Запуск: pytest tests/test_ai_core.py -v
"""
from src.ai_core import extract_json_data


class TestExtractJsonData:

    def test_valid_json_response(self):
        """
        AI вернул правильный JSON.

        Подсказка:
        1. text = '{"reasoning": "test", "short_desc": "nginx port conflict", "script": "#!/bin/bash\\necho ok"}'
        2. desc, script = extract_json_data(text)
        3. assert desc == "nginx port conflict"
        4. assert "echo ok" in script
        """
        # Твой код здесь...
        pass

    def test_json_wrapped_in_markdown(self):
        """
        AI обернул JSON в ```json ... ``` (часто бывает).

        Подсказка: оберни тот же JSON:
        text = '```json\\n{"reasoning": "x", "short_desc": "desc", "script": "echo hi"}\\n```'
        и проверь, что парсер достанет данные.
        """
        # Твой код здесь...
        pass

    def test_manual_intervention_response(self):
        """AI сказал, что нужно ручное вмешательство."""
        desc, script = extract_json_data("MANUAL_INTERVENTION_REQUIRED")
        assert script == "MANUAL_INTERVENTION_REQUIRED"
        # Подсказка: проверь ещё desc — что он содержит слово "Manual"
        # Твой assert здесь...

    def test_garbage_input(self):
        """
        AI вернул полную чушь — не JSON, не ключевое слово.

        Подсказка: посмотри в код extract_json_data() —
        если нет JSON и нет MANUAL_INTERVENTION_REQUIRED,
        возвращается ("AI response parsing error", text.strip())
        """
        desc, script = extract_json_data("lol I am not json")
        # Твои assert'ы здесь...
        pass

    def test_invalid_json(self):
        """
        AI вернул что-то похожее на JSON, но сломанное.

        Подсказка: json.loads упадёт → ветка except JSONDecodeError
        → возвращается ("JSON reading error", text.strip())
        """
        desc, script = extract_json_data('{not valid json at "all}')
        # Твои assert'ы здесь...
        pass
