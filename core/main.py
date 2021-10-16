from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Core Service'}


register_tortoise(
    app,
    db_url='postgres://postgres:s3cret@localhost:5432/teachio',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
