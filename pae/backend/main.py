from fastapi import FastAPI
from pae.backend.routes import courses_routes, prereq_routes

app = FastAPI(title="PAE Manager API", version="1.0.0")

app.include_router(courses_routes.router)
app.include_router(prereq_routes.router)
