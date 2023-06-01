from sqlalchemy import Optional, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    genre: Mapped[Optional[str]] = mapped_column(String(30))
    url: Mapped[Optional[str]] = mapped_column(String(100))


class Game(Base):
    __tablename__ = "game"


class Movie(Base):
    __tablename__ = "movie"


class Series(Base):
    __tablename__ = "series"


class Band(Base):
    __tablename__ = "band"


class Album(Base):
    __tablename__ = "album"
