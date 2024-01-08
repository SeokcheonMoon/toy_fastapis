from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr
class User_name(Document):
    _id : Optional[str] = None
    player_name : Optional[str] = None
    answer: Optional[str] = None
    point: Optional[int] = None
    player_answer: Optional[str] = None

    class Settings:
        name = "user_name"
