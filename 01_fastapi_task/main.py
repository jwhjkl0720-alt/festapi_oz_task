from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello world"}


@app.get("/Hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello{name}"}


def add(a: int, b: int) -> None:
    return a + b
