from fastapi import APIRouter,HTTPException
from pae.backend.models.prereq import Prereq
from pae.backend.service.neo4j_service import (
add_prereq,
get_all,
delete_prereq,
)

router = APIRouter(prefix="/prereq", tags=["prereq"])

@router.post("/",response_model=dict)
def create_prereq(prereq: Prereq):
    try:
        message = add_prereq(course_acronym=prereq.course_acronym,prereq_acronym=prereq.prereq_acronym)
        return {"message":message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Neo4j : {str(e)}")


@router.get("/{course_acronym}",response_model=dict)
def list_prereqs(course_acronym: str):
    try:
        prereqs = get_all(course_acronym=course_acronym)
        return {
        "course": course_acronym,
        "prereqs":prereqs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Neo4j : {str(e)}")

@router.delete("/",response_model=dict)
def delete_pre(prereq: Prereq):
    try:
        message = delete_prereq(course_acronym=prereq.course_acronym,prereq_acronym=prereq.prereq_acronym)
        return {"message":message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur Neo4j : {str(e)}")