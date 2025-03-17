from pydantic import BaseModel


class QuizRead(BaseModel):
    quiz: dict


class QuizRequest(BaseModel):
    quiz: str = ""
