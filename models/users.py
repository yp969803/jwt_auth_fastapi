from sqlalchemy import(
    LargeBinary,
    Column,
    String,
    Integer,
    Boolean,
    UniqueConstraint,
    PrimaryKeyConstraint
)

from pydantic import BaseModel, Field, EmailStr

import bcrypt

import jwt;

from db_initializer import Base 

class User(Base):
    """Modelsa user table"""
    __tablename__="users"
    email=Column(String(225), nullable=False, unique=True)
    id= Column(Integer, nullable=False, primary_key=True)
    hashed_password = Column(LargeBinary, nullable=False)
    full_name = Column(String(225), nullable=False)
    is_active = Column(Boolean, default=False)

    UniqueConstraint("email", name="uq_user_email")
    PrimaryKeyConstraint("id", name="pk_user_id")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<User {full_name!r}>".format(full_name=self.full_name)
    
    @staticmethod
    def hash_password(password) -> str:
        """Tranaforms password from it's raw textual form to cryptographic hashes"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def validate_password(self, password) -> bool:
        """Confirms password validity"""
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password)
    
    def generate_token(self) -> dict :
        """Generate access token for user"""
        return {
              "access_token": jwt.encode(
                {"full_name": self.full_name, "email": self.email},
                "ApplicationSecretKey"
            )
        }



