from fastapi import APIRouter

from schemas.chat import ChatRequest, ChatResponse
from services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    chat_service = ChatService()
    answer = await chat_service.chat(request.message)
    return ChatResponse(answer=answer)