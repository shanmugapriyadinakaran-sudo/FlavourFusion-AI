from fastapi import APIRouter
from app.schemas.all_schemas import AssistantChatRequest, AssistantChatResponse
from app.services.assistant_engine import AssistantEngine

router = APIRouter(prefix="/assistant", tags=["AI Assistant"])
engine = AssistantEngine()

@router.post("/chat", response_model=AssistantChatResponse)
def assistant_chat(payload: AssistantChatRequest):
    """
    Interactive culinary AI assistant ("Chef Fusion AI") endpoint.
    Handles food chemistry questions, flavor illusions, midnight snack cravings,
    and returns 1-click loadable ingredient pairings.
    """
    return engine.chat(payload.message, payload.current_ingredients)
