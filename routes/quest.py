from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from beanie import PydanticObjectId

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

from databases.quest_connections import Quest_Database
from models.users import Quiz

collection_quiz = Quest_Database(Quiz)

@router.get("/quiz_solve") # 펑션 호출 방식
async def quiz_solve(request:Request):
    quiz_list = await collection_quiz.get_all()
    return templates.TemplateResponse(name="quest/quiz_solve.html", context={'request':request, "quizs" :quiz_list})




from models.user_name import User_name

collection_user_name = Quest_Database(User_name)

@router.post("/quiz_solve") # 펑션 호출 방식
async def user_name_input(request:Request):
    form_data = await request.form()
    user_form_data = dict(form_data)
    user = User_name(**user_form_data)
    await collection_user_name.save(user)
    user_form_data = await collection_user_name.get()
    return templates.TemplateResponse(name="quest/quiz_solve.html", context={'request':request, "user_name" :user_form_data})



# @router.get("/search") # 검색
# async def list(request:Request):
#     user_dict = dict(request._query_params)
#     print(user_dict)
#     # { 'name': { '$regex': user_dict.word } }
#     conditions = { user_dict['key'] : { '$regex': user_dict["word"] } }

#     user_name_list = await collection_user_name.getsbyconditions(conditions)
#     return templates.TemplateResponse(name="users/list_jinja.html"
#                                       , context={'request':request
#                                                  , 'player_name' : user_name_list })

# @router.get("/quiz_solve") # 펑션 호출 방식
# async def quiz_solve(request:Request):
#     user_name = await collection_user_name.get_all()
#     return templates.TemplateResponse(name="quest/quiz_solve.html", context={'request':request, "name" :user_name})


# @router.post("/quiz_solve") # 펑션 호출 방식                                                                      가입부분은 post로 넘겨야함.
# async def player_list_post(request:Request,):
#     form_data = await request.form()
#     question_id = form_data.get('question_id')
#     quiz = await Quiz.get(PydanticObjectId(question_id))
#     player_list = {
#         'question_id': question_id,
#         'player_name': form_data.get('player_name'),
#         'correct_answer': quiz.answer if quiz else None,
#         'point': int(quiz.point),
#         'player_answer': form_data.get('player_answer')
#     }
#     player = Player(**player_list)
#     await player.insert()
#     #리스트 정보
#     player_list = await player.find_all().to_list()
#     return templates.TemplateResponse(name="quest/player_list.html", context={'request':request, "players" : player_list})


@router.get("/player_list") # 펑션 호출 방식
async def player_list(request:Request):
    player_list = await collection_player.get_all()
    return templates.TemplateResponse(name="quest/player_list.html", context={'request':request, "players" :player_list})

