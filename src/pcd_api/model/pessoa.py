from sqlalchemy import Column, Integer, String
from pcd_api.model.base import Base

class Pessoa(Base):
    
    __tablename__ = "pessoa"
    
    nome = Column(String(60))
    id = Column(Integer, primary_key = True, index = True)
    cpf = Column(Integer, primary_key = True, index = True)
    email = Column(String(100))
    cid = Column(String(15))
    senha = Column(String(80))
    dt_cadastro = Column(String(10))
    deficiencia_id = Column(Integer, primary_key = True, index = True)
    