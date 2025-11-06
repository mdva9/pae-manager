
from pae.backend.models.prereq import Prereq
from pae.backend.db_neo4j import get_neo4j_driver
from neo4j import GraphDatabase


driver = get_neo4j_driver()

#Add Prereq
def add_prereq(course_acronym:str,prereq_acronym:str):

    if not course_acronym or not prereq_acronym:
        raise ValueError("Les acronymes ne peuvent pas être vides.")

    query = """
       MERGE (p:Course {acronym: $prereq})
         ON CREATE SET p.is_prereq = true
       MERGE (c:Course {acronym: $course})
         ON CREATE SET c.is_prereq = false
       MERGE (p)-[:IS_PREREQUISITE_OF]->(c)
       RETURN p, c
       """
    with driver.session() as session:
        session.run(query,course=course_acronym,prereq=prereq_acronym)

    return f"Relation add : {prereq_acronym} -> {course_acronym}"

#Get All Prereq
def get_all(course_acronym: str):
    query = """
           MATCH (p:Course)-[:IS_PREREQUISITE_OF]->(c:Course {acronym: $course})
           RETURN p.acronym AS prerequisite
           """
    with driver.session() as session:
        results = session.run(query, course=course_acronym)
        prereqs = [record["prerequisite"] for record in results]
    return prereqs

def delete_prereq(course_acronym:str,prereq_acronym:str):
    query = """
       MATCH (p:Course {acronym: $prereq})-[r:IS_PREREQUISITE_OF]->(c:Course {acronym: $course})
       DELETE r
       """
    with driver.session() as session:
        session.run(query, course=course_acronym,prereq=prereq_acronym)
    return f"Relation Deleted : {prereq_acronym} -> {course_acronym}"