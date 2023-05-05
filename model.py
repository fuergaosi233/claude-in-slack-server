from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel

class ConversationRequest(BaseModel):
    prompt: str
    conversation_id: Optional[str]


class ConversationResponse(BaseModel):
    message: str
    conversation_id: Optional[str]
    error: Optional[str]
