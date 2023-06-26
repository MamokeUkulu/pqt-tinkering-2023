from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy import Column, Integer, String, Boolean

engine = create_engine("sqlite://", echo=True)

class Base(DeclarativeBase):
    pass

# Db model
class Todo(Base):
    __tablename__ = "todo"
    id: Mapped[int] = mapped_column(primary_key=True)
    complete: Mapped[bool] = mapped_column(Boolean)
    text: Mapped[str] = mapped_column(String(30))
    def __repr__(self):
        return "<User(complete='%s', text='%s')>" % (
            self.complete,
            self.text,
        )
    
def build_tables():
   Base.metadata.create_all(engine)
#    pass
    
# db repo
def create_all(todos: List[Todo]):
    with Session(engine) as session:
        todolist = [Todo(complete=t.complete, text=t.text) for t in todos]
        session.add_all(todolist)
        session.commit()

def find_all() -> List[Todo]:
    with Session(engine) as session:
        return session.query(Todo).all()