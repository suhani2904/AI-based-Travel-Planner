from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field

class Place(BaseModel):
    name: str = Field(description= "name of the place")
    category : List[str] = Field(description="select category / categories given in the preferneces")

class PlacesOutput(BaseModel):
    places: List[Place]

parser_1 = PydanticOutputParser(pydantic_object=PlacesOutput)


class all_places(BaseModel):
    name : str = Field(description= "name of the place")
    rating : float = Field(lt = 5 , gt = 1, description="rating of the place")
    ticket : float = Field(description="ticket of the place")

class all_places_output(BaseModel):
    places : List[all_places]

parser_2 = PydanticOutputParser(pydantic_object=all_places_output)