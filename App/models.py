from pydantic import BaseModel
from typing import List

class PromptInput(BaseModel):
    topic: str
    tone: str
    style: str
    keywords: List[str]
    output_type: str