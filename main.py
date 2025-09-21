from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Movie Catalog API is running 🚀"}


@app.get("/movies/")
def movies():
    pass


@app.get("/movies/{id}")
def movies_id():
    pass


@app.post("/movies/")
def create_movie():
    pass


@app.put("/movies/{id}")
def update_movie():
    pass


@app.delete("/movies/{id}")
def delete_movie():
    pass
