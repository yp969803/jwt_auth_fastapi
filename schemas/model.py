from pydantic import BaseModel, Field, EmailStr
class QuestionSchema(BaseModel):
    question: str
   

class LinkSchema(BaseModel):
    link: str