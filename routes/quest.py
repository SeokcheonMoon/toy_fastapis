from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

@router.post("/quiz_solve", response_class=HTMLResponse) # 펑션 호출 방식
async def insert(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="quest/quiz_solve.html", context={'request':request})

@router.get("/quiz_solve") # 펑션 호출 방식                                                                      가입부분은 post로 넘겨야함.
async def insert_post(request:Request):
    # user_dict = dict(await request.form())
    # print(user_dict)
    # #저장
    # user = User(**user_dict)
    # await collection_user.save(user)
    # print(user_dict)
    # #리스트 정보
    # user_list = await collection_user.get_all()
    return templates.TemplateResponse(name="quest/quiz_solve.html", context={'request':request})


from databases.connections import Database
from models.users import Quiz

cllection_user = Database(Quiz)

@router.get("/list") # 펑션 호출 방식
async def list(request:Request):
    # print(dict(request._query_params))
    # user_list = [
    #     {"id": 1, "name": "김철수", "email": "cheolsu@example.com"},
    #     {"id": 2, "name": "이영희", "email": "younghi@example.com"},
    #     {"id": 3, "name": "박지성", "email": "jiseong@example.com"},
    #     {"id": 4, "name": "김미나", "email": "mina@example.com"},
    #     {"id": 5, "name": "장현우", "email": "hyeonwoo@example.com"}
    # ]
    # insert 작업 진행
    # documents = collection.find({})
    #document.next() = 오류 확인용
# cast cursor to list
    user_list = await collection_quiz.get_all()
    # for document in documents:
    #     print("document : {}".format(document))
    #     user_list.append(document)
    #     pass
    # # return templates.TemplateResponse(name="users/list.html", context={'request':request, "users" :user_list})
    return templates.TemplateResponse(name="users/list_jinja.html", context={'request':request, "users" :user_list})