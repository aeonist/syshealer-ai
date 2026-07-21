"""
Ленивая инициализация базы данных.
Движок и сессии создаются НЕ при импорте, а при первом вызове.

🖊️ НАПИШИ САМ — заполни функции get_engine(), _get_session_factory(), get_session()
Подсказки написаны в docstring каждой функции.
"""
import os
from contextlib import contextmanager
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    String,
    Text,
    create_engine,
    func,
    text,
)
from sqlalchemy.engine import Engine, make_url
from sqlalchemy.orm import (
    Mapped,
    declarative_base,
    mapped_column,
    sessionmaker,
)

from src.config import BASE_DIR, load_config

Base = declarative_base()


# ============================================================
# МОДЕЛЬ — перенесена из старого database.py без изменений
# ============================================================
class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    raw_log: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String, default="pending", nullable=False)
    ai_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    log_hash: Mapped[str | None] = mapped_column(
        String, unique=True, index=True, nullable=True
    )
    occurrences: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    attempt: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    executed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    ai_log_review: Mapped[str | None] = mapped_column(Text, nullable=True)


# ============================================================
# ЛЕНИВЫЙ ДВИЖОК
# ============================================================
_engine: Engine | None = None


def get_engine() -> Engine:
    """
    Возвращает движок БД, создавая его при первом вызове.

    Подсказка:
    1. Используй `global _engine`
    2. Если _engine уже не None — просто верни его (кеширование)
    3. Прочитай конфиг через load_config()
    4. Если db_type == "sqlite":
       - db_path = os.path.join(BASE_DIR, "syshealer.db")
       - _engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False})
    5. Иначе (postgres):
       - Загрузи .env через load_dotenv(os.path.join(BASE_DIR, ".env"))
       - Прочитай DATABASE_URL из os.getenv("DATABASE_URL")
       - Если DATABASE_URL нет — raise RuntimeError("DATABASE_URL is required for PostgreSQL")
       - _engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=5)
    6. Верни _engine

    ВАЖНО: НЕ используй sys.exit(). Используй raise RuntimeError(...).
    """
    # Твой код здесь...
    pass


# ============================================================
# ЛЕНИВЫЕ СЕССИИ
# ============================================================
_SessionFactory = None


def _get_session_factory():
    """
    Создаёт и кеширует фабрику сессий.

    Подсказка:
    1. global _SessionFactory
    2. Если _SessionFactory уже не None — верни его
    3. engine = get_engine()
    4. Base.metadata.create_all(bind=engine)   ← создаёт таблицы
    5. _SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    6. Верни _SessionFactory
    """
    # Твой код здесь...
    pass


@contextmanager
def get_session():
    """
    Context manager для безопасной работы с БД.

    Использование:
        with get_session() as db:
            db.query(Incident).all()

    Подсказка — структура:
    1. factory = _get_session_factory()
    2. session = factory()     ← создаём новую сессию
    3. try:
    4.     yield session        ← передаём управление вызывающему коду
    5.     session.commit()     ← если код не упал — сохраняем изменения
    6. except Exception:
    7.     session.rollback()   ← если упал — откатываем
    8.     raise                ← пробрасываем ошибку дальше
    9. finally:
    10.    session.close()      ← в любом случае закрываем соединение
    """
    # Твой код здесь...
    pass
