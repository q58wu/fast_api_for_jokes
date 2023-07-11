from uuid import uuid4

from pydantic import BaseModel, Field, UUID4


class Joke(BaseModel):
    jokeHeader: str
    punchLine: str