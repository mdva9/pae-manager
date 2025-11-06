from pydantic import BaseModel, Field
from typing import List,Optional

class Course(BaseModel):
    acronym: str = Field(..., example="2DON1",description="Acronyme du cours")
    title: str = Field(...,example="Base de données 1", description="Titre du cours")
    ects: int = Field(..., gt=0, le=30, example=5, description="Nombre de crédits ECTS")
    block : int =  Field(..., ge=1, le=5, example=2, description="Numéro du bloc (1, 2 ou 3)")
    professors: Optional[List[str]] = Field(default_factory=list, description="Liste des professeurs du cours")


    class Config:
        schema_extra = {
            "example": {
            "acronym": "3DEV3",
            "title": "Développement 3",
            "ects": 5,
            "block": 3,
            "professors": ["Romain Absil", "Quentin Houben"]
            }
        }

