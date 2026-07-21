"""
Безопасное выполнение bash-скриптов.

🖊️ НАПИШИ САМ — заполни методы save_script() и execute()
Подсказки написаны в docstring каждого метода.
"""
import os
import subprocess
import uuid
from dataclasses import dataclass
from pathlib import Path

from src.core.logger import get_logger

logger = get_logger(__name__)


@dataclass
class ExecutionResult:
    """Результат выполнения скрипта."""

    success: bool  # Скрипт завершился с кодом 0?
    exit_code: int  # Код выхода bash (0 = ок, всё остальное = ошибка)
    output: str  # Весь вывод (stdout + stderr)


class ScriptExecutor:
    """
    Выполняет bash-скрипты безопасно.

    Подсказки:
    - Используй subprocess.run() вместо os.system()
    - subprocess.run() позволяет: задать таймаут, перехватить вывод,
      НЕ использовать shell (безопаснее)
    - os.system() просто прокидывает строку в bash, и если в пути есть
      спецсимвол (;, |, &&) — это shell injection уязвимость
    """

    TIMEOUT: int = 300  # 5 минут

    def save_script(self, content: str, incident_id: int, base_dir: str) -> Path:
        """
        Сохраняет скрипт на диск и делает его исполняемым.

        Подсказка:
        1. Создай директорию:
           script_dir = os.path.join(base_dir, "data", "scripts")
           os.makedirs(script_dir, exist_ok=True)

        2. Сгенерируй уникальное имя:
           script_id = uuid.uuid4().hex[:8]
           filename = f"fix_incident_{incident_id}_{script_id}.sh"
           script_path = Path(os.path.join(script_dir, filename))

        3. Если content не начинается с "#!" — добавь shebang:
           if not content.startswith("#!"):
               content = "#!/bin/bash\n\n" + content

        4. Запиши файл:
           script_path.write_text(content + "\n", encoding="utf-8")

        5. Сделай исполняемым:
           os.chmod(script_path, 0o755)

        6. Залогируй:
           logger.info("Script saved: %s", script_path)

        7. return script_path
        """
        # Твой код здесь...
        pass

    def execute(self, script_path: Path, capture_output: bool = True) -> ExecutionResult:
        """
        Выполняет скрипт через subprocess.

        Подсказка:
        1. Используй subprocess.run():
           result = subprocess.run(
               ["sudo", str(script_path)],
               capture_output=True,   # перехватить stdout и stderr
               text=True,             # вернуть строки, а не байты
               timeout=self.TIMEOUT,  # убить если висит дольше 5 минут
           )

        2. Обработай TimeoutExpired:
           try:
               result = subprocess.run(...)
           except subprocess.TimeoutExpired:
               logger.error("Script timed out after %d seconds", self.TIMEOUT)
               return ExecutionResult(success=False, exit_code=-1, output="TIMEOUT")

        3. Собери вывод:
           output = (result.stdout or "") + (result.stderr or "")

        4. Залогируй:
           logger.info("Script %s finished with exit code %d", script_path, result.returncode)

        5. return ExecutionResult(
               success=(result.returncode == 0),
               exit_code=result.returncode,
               output=output,
           )
        """
        # Твой код здесь...
        pass
