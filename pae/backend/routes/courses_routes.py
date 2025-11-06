from fastapi import APIRouter,HTTPException
from typing import List
from pae.backend.models.course import Course
from pae.backend.service.mongo_service import (
add,
delete_course,
find_course_by_acronym,
update_course,
all_course
)
router = APIRouter(prefix="/courses", tags=["courses"])


# Add Course
@router.post("/",response_model=dict)
def create_course(course: Course):
    try:
        course_id = add(course)
        return {"message":f"Cours ajouté avec succès.", "id": course_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur interne : {str(e)}")

# Get all course
@router.get("/",response_model=List[Course])
def get_all_courses():
    return all_course()

@router.get("/{acronym}",response_model=Course)
def get_course(acronym: str):
    course = find_course_by_acronym(acronym)
    if not course:
        raise HTTPException(status_code=404,detail=f"Course not found{acronym}")
    return course


@router.put("/{acronym}")
def update(acronym: str, course: Course):
    success = update_course(acronym,course.dict())
    if not success:
        raise HTTPException(status_code=404,detail=f"Course not found{acronym}")
    return {"message":f"{acronym} is update "}

@router.delete("/{acronym}",response_model=dict)
def delete(acronym: str):
    success = delete_course(acronym)
    if not success:
        raise HTTPException(status_code=404,detail=f"Course not found{acronym}")
    return {"message":f"Course {acronym} was deleted"}