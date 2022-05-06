import os
import asyncio
import aiohttp
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv

from models import Question
from models import Question as ModelQuestion

from schema import Question as SchemaQuestion
from schema import ReqQuestion as SchemaReqQuestion

load_dotenv('.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DB_URL'])

URL = 'https://jservice.io/api/random?'
REMAINED_QS = 0


@app.get('/')
async def root():
    return {'message': 'Welcome to the service :)'}


async def get_request_data(async_session, url, existing_jsids, is_first):
    async with async_session.get(url) as response:
        if response.content_type == 'application/json':
            response_json = await response.json()
            for element in response_json:
                db_quest = ModelQuestion(question_text=element['question'],
                                         answer_text=element['answer'],
                                         created_at=element['created_at'],
                                         jservice_id=element['id'])
                global REMAINED_QS
                if db_quest.jservice_id not in existing_jsids:
                    db.session.add(db_quest)
                    existing_jsids.add(db_quest.jservice_id)
                    if not is_first:
                        REMAINED_QS -= 1
                elif is_first:
                    REMAINED_QS += 1


async def gather_data(cnt, existing_jsids, is_first):
    async with aiohttp.ClientSession() as async_session:
        tasks = []
        while cnt:
            if cnt <= 100:
                task = asyncio.create_task(
                    get_request_data(async_session, f'{URL}count={cnt}', existing_jsids, is_first)
                )
                cnt -= cnt
            else:
                task = asyncio.create_task(
                    get_request_data(async_session, f'{URL}count=100', existing_jsids, is_first)
                )
                cnt -= 100
            tasks.append(task)
        await asyncio.gather(*tasks)


@app.post('/add-questions/', response_model=SchemaQuestion)
async def add_questions(question: SchemaReqQuestion):
    size = db.session.query(Question).count()
    existing_jsids = set(el[0] for el in db.session.query(Question.jservice_id).all())
    amt = question.questions_num
    await gather_data(amt, existing_jsids, True)
    global REMAINED_QS
    while REMAINED_QS:
        await gather_data(REMAINED_QS, existing_jsids, False)
    db.session.commit()
    is_commited_new_lines = db.session.query(Question).count() - size
    return db.session.query(Question).all()[-1] if is_commited_new_lines else None


@app.get('/questions/')
async def get_questions():
    questions = db.session.query(Question).all()
    return questions


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
