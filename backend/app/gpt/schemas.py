from pydantic import BaseModel


class QuizRead(BaseModel):
    quiz: list
