from pydantic import BaseModel, Field

class Prereq(BaseModel):
    course_acronym: str = Field(...,example="3DEV3", description="Cours qui a un prérequis")
    prereq_acronym: str = Field(..., example="2DEV2", description="Cours requis pour y accéder")

    class Config:

        schema_extra = {
            "example": {
                "course_acronym": "3DEV3",
                "prerequisite_acronym": "2DEV2"
            }
        }