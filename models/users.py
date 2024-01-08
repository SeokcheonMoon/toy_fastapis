from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field를 제한
class User(Document):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    pswd: Optional[str] = None
    manager: Optional[str] = None
    sellist1 : Optional[str] = None
    text : Optional[str] = None
  
    class Settings:
        name = "users"


class Quiz(Document):
    question: Optional[str] = None
    choice1: Optional[str] = None
    choice2: Optional[str] = None
    choice3: Optional[str] = None
    choice4: Optional[str] = None
    answer: Optional[str] = None
    point: Optional[int] = None
  
    class Settings:
        name = "quiz"

class User_name(Document):
    player_name : Optional[str] = None

    class Settings:
        name = "user_name"


class Player(Document):
    _id : Optional[str] = None
    _id : Optional[str] = None
    player_name : Optional[str] = None
    answer: Optional[str] = None
    point: Optional[int] = None
    player_answer: Optional[str] = None

    class Settings:
        name = "player"
