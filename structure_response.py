from pydantic import BaseModel, Field
from typing import List

from llm import llm_by_deepseek, llm_by_openai
class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    genre: str = Field(description="The genre of the movie")
    rating: float = Field(description="The rating of the movie")
    description: str = Field(description="The description of the movie")
    director: str = Field(description="The director of the movie")
    actors: List[str] = Field(description="The actors in the movie")
    plot: str = Field(description="The plot of the movie")
    poster: str = Field(description="The poster of the movie")
    trailer: str = Field(description="The trailer of the movie")
    reviews: List[str] = Field(description="The reviews of the movie")
    similar_movies: List[str] = Field(description="The similar movies of the movie")


model_with_structured_output = llm_by_openai.with_structured_output(Movie)

response = model_with_structured_output.invoke("我想要一部关于爱情的电影，请推荐一部")