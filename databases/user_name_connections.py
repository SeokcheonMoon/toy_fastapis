from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.users import User_name
from motor.motor_asyncio import AsyncIOMotorClient
# from pydantic import BaseModel
# 변경 후 코드
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL : Optional[str] = None
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[User_name])
    
    class Config:
        env_file = ".env"

class user_name_Database :
    #model은 collection
    def __init__(self, model) -> None:
        self.model = model
        pass

    async def get_all(self) :
        documents = await self.model.find_all().to_list()
        return documents
    
    # 상세 보기
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)  
        if doc:
            return doc
        return False
    
    # column 값으로 여러 Documents 가져오기
    async def getsbyconditions(self, conditions:dict) -> [Any]:
        documents = await self.model.find(conditions).to_list()  # find({})
        if documents:
            return documents
        return False    
    
    # 저장
    async def save(self, document) -> None:
        await document.create()
        return None