```
~$ pip install fastapi uvicorn jinja2
~$ pip install python-multipart

```

### Quest Mission ###
- refer : screen definition
- 문제 작성(4지 선다형, 5문항, 문항마다 다른 점수, 정답 입력) : 미리 입력 -> List 작성
- 응시자 문제 풀기 : 응시자 이름 입력, 문제 풀기 -> List 이동
- Dabase 설계 규칙 : 한 shell에는 묶음 datatype 안 넣기
- 산출물 : README.md(구성원별 역할 기록), 동작 url, github 링크

|구분|내용|비고|
| -- | -- | -- | 
|Database 명칭| toy_fastapis | -- |
|문제 Collection | quiz | 구성 : id, 문제, 보기, 정답번호 |
|응시자 Collection | player | 구성 : object_id,퀴즈 id, 응시자이름, 각 문제당 응답번호 |

| 페이지 출력 관련 | 페이지 명칭 | 담당자 |
|문제 리스트와 선택지 리스트 산출 | quiz_list |  --  |
| 문제 풀기  | quiz_solve | -- |
| 참가자 및 결과 | player_list | -- |