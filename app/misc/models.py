from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import List

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    uuid: Mapped[str] = mapped_column(primary_key=True, unique=True, index=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(80))

    # todos: Mapped[List['Todo']]
    tasks: Mapped[List['Task']] = relationship(back_populates='user', cascade='all, delete-orphan')

#class Todo
class Task(Base):
    __tablename__ = 'tasks'#'todos'

    user_uuid: Mapped[str] = mapped_column(ForeignKey('users.uuid'))
    user: Mapped['User'] = relationship(back_populates='tasks')#'todos')
    
    # todo_id: 
    task_id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True, autoincrement=True)

    title: Mapped[str] = mapped_column(default=None)
    text: Mapped[str] = mapped_column(default=None)
