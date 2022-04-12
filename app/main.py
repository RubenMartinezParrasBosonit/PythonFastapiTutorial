import uvicorn
from fastapi import FastAPI
from . import model
from .connection import engine
from .routers import blog, user, authentication
from starlette.responses import RedirectResponse

model.base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

@app.get("/",
         description="Comenta/Descomenta los app.include_router en main.py para ver solo las tablas que estás utilizando")
def main():
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)