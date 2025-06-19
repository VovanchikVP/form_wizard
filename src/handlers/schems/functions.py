from pydantic import BaseModel


class Argument(BaseModel):
    type: str
    description: str


class Parameters(BaseModel):
    type: str = "object"
    properties: dict[str, Argument]
    required: list[str]


class Function(BaseModel):
    name: str = "generate_template"
    file_path: str
    description: str
    parameters: Parameters
