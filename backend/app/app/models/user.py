from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class User(Base):
    id = Column(Integer,primary_key=True)
    userType =Column(TINYINT,comment="1->Admin,2->User")
    name = Column(String(200))
    email = Column(String(255))
    phone = Column(String(20))
    alternativeNumber =Column(String(20))
    password = Column(String(255))
    image =Column(String(255))
    otp = Column(String(20))
    otpExpireAt = Column(DateTime)
    otpVerifiedStatus = Column(TINYINT, default = 0, comment="0->No, 1->Yes")
    otp_verified_at = Column(DateTime)
    reset_key=Column(String(255))
    created_at=Column(DateTime)
    updated_at=Column(DateTime)
    status=Column(TINYINT,comment="-1->delete,1->active,0->inactive")

    api_tokens=relationship("ApiTokens",back_populates="user")
    
    
    
