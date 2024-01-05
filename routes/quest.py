from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# @router.post("/quiz_solve", response_class=HTMLResponse) # 펑션 호출 방식
# async def insert(request:Request):
#     await request.form()
#     print(dict(await request.form()))
#     return templates.TemplateResponse(name="quest/quiz_solve.html", context={'request':request})

# @router.get("/quiz_solve") # 펑션 호출 방식                                                                      가입부분은 post로 넘겨야함.
# async def insert_post(request:Request):
#     # user_dict = dict(await request.form())
#     # print(user_dict)
#     # #저장
#     # user = User(**user_dict)
#     # await collection_user.save(user)
#     # print(user_dict)
#     # #리스트 정보
#     # user_list = await collection_user.get_all()
#     return templates.TemplateResponse(name="quest/quiz_solve.html", context={'request':request})


from databases.quest_connections import Quest_Database
from models.users import Quiz

collection_quiz = Quest_Database(Quiz)

@router.get("/quiz_solve") # 펑션 호출 방식
async def list(request:Request):

    quiz_list = await collection_quiz.get_all()
    return templates.TemplateResponse(name="quest/quiz_solve.html", context={'request':request, "quizs" :quiz_list})