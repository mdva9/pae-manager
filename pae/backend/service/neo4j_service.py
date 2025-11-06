
from pae.backend.models.prereq import Prereq
from pae.backend.db_neo4j import get_neo4j_driver
from neo4j import GraphDatabase


driver = get_neo4j_driver()

#Add Prereq
def add_prereq(course_acronym:str,prereq_acronym:str):

    query="""
    MERGE (c:Course {course_acronym: $course})
    MERGE (p:Course {prereq_acronym: $prereq})
    MERGE (p)-[:IS_PREREQ_OF]->(c)
    """

    with driver.session() as session:
        session.run(query,course=course_acronym,prereq=prereq_acronym)

    return f"Relation add : {prereq_acronym} -> {course_acronym}"

#Get All Prereq
def get_all(course_acronym: str):
    query = """
    MATCH (p:Course)-[:IS_PREREQ_OF]->(c:Course {acronym: $course})
    RETURN p.acronym AS prerequisite
    """
    with driver.session() as session:
        results = session.run(query, course=course_acronym)
        prereqs = [record["prereq"] for record in results]
    return prereqs

def delete_prereq(course_acronym:str,prereq_acronym:str):

    query= """
    MATCH (p:Course {acronym: $prerequisite})-[r:IS_PREREQ_OF]->(c:Course {acronym: $course})
    DELETE r
    """

    with driver.session() as session:
        session.run(query, course=course_acronym,prereq=prereq_acronym)
    return f"Relation Deleted : {prereq_acronym} -> {course_acronym}"