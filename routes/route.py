from typing import Optional

from fastapi import APIRouter
from models.Joke import Joke
from config.database import jokesCollection
from schema.schema import joke_serialize_list_to_get, joke_serialize_to_post

router = APIRouter()


@router.get("/")
async def get_jokes(max_item_count: Optional[str] = 5):
    jokes = joke_serialize_list_to_get(jokesCollection.aggregate([{'$sample': {'size': int(max_item_count)}}]))
    return jokes



@router.post("/")
async def post_joke(joke: Joke):
    jokesCollection.insert_one(joke_serialize_to_post(joke))
