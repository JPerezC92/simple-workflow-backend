import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise  # type: ignore

import env_vars
from boards.infrastructure.boards_router import boards_router
from phases.infrastructure.phases_router import phases_router

app = FastAPI()

app.include_router(phases_router)
app.include_router(boards_router)

register_tortoise(
    app,
    db_url=env_vars.database_url,
    modules={"models": ["db.boards_db", "db.phases_db"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    load_dotenv()

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
