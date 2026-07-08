from pydantic import BaseModel, EmailStr, Field

class Employee(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18, le=60)
    salary: float = Field(gt=0)