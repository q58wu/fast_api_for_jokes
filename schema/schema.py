from models import Joke


def joke_serialize_to_post(joke: Joke) -> dict:
    return {
        "joke": joke.jokeHeader,
        "punchLine": joke.punchLine
    }


def joke_serialize_to_get(joke: Joke) -> dict:
    return {
        "id": str(joke['_id']),
        "joke": joke['joke'],
        "punchLine": joke['punchLine']
    }


def joke_serialize_list_to_get(jokes: list[Joke]) -> list:
    return [joke_serialize_to_get(joke) for joke in jokes]
