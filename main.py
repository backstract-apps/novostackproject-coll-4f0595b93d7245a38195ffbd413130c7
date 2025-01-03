from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novostackproject-coll-4f0595b93d7245a38195ffbd413130c7',debug=False,docs_url='/quirky-johnson-f5320774c9d811efbee00242ac12000421/docs',openapi_url='/quirky-johnson-f5320774c9d811efbee00242ac12000421/openapi.json')

app.include_router(router, prefix='/quirky-johnson-f5320774c9d811efbee00242ac12000421/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()