from typing import List, Optional
from pae.backend.models.course import Course
from pae.backend.db_mongo import get_mongo_client


# MongoDB
client = get_mongo_client()
db = client['pae-manager']
courses = db['courses']

# Add course
def add (course:Course) -> str:
    if courses.find_one({"acronym": course.acronym}) is None:
        raise ValueError(f"Le cours {course.acronym} est déjà présent")

    result = courses.insert_one(course.dict())
    return str(result.inserted_id)

# get Courses
def all_course()->List[dict]:
    course_list = list(courses.find({},{"_id":0}))
    return course_list

# Find Course
def find_course_by_acronym (acronym: str) -> Optional[dict]:
    course = courses.find_one({"acronym": acronym}).id({"_id": 0})
    return course

# Update Course
def update_course(acronym: str, data: dict) -> bool:
    result = courses.update_one({"acronym": acronym}, {"$set": data})
    return result.modified_count > 0

# Delete Course
def delete_course(acronym: str) -> bool:
    result = courses.delete_one({"acronym": acronym})
    return result.deleted_count > 0