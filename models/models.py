from sqlalchemy.orm import mapped_column, Mapped, declarative_base, Session
from sqlalchemy import Integer, String, Date, Float, VARCHAR, DECIMAL, create_engine
from datetime import date
from flask_login import UserMixin

engine = create_engine('mysql://root:@localhost/db_atividade17')

Base = declarative_base()

class User(Base,UserMixin):
    __tablename__ = 'usuarios'

    id_user:Mapped[int] = mapped_column(Integer, primary_key=True)
    Nome_usuario:Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    email:Mapped[str] = mapped_column(VARCHAR(255), nullable=False, unique=True)
    senha : Mapped[int] = mapped_column(VARCHAR(60), nullable= False)
    Numero_telefone:Mapped[str] = mapped_column(VARCHAR(15), nullable=False)
    data_inscricao:Mapped[date] = mapped_column(Date, nullable=False)
    multa_atual:Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=True)

    @classmethod
    def get(cls, user_id):
        with Session(bind = engine) as sessao:
            obj = sessao.query(User).where(User.id_user == user_id).first()
            sessao.close()
            return obj
