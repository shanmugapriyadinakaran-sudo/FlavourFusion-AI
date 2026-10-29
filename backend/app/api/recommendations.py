from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.entities import User, UserRating
from app.schemas.all_schemas import RecommendationItem, RecommendationFeedbackRequest
from app.services.recommendation_engine import RecommendationEngine
from app.api.deps import get_current_user_optional, get_current_user

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.get("/personalized", response_model=List[RecommendationItem])
def get_personalized_recommendations(
    cuisine: Optional[str] = Query(None),
    novelty: Optional[str] = Query(None),
    limit: int = Query(6, ge=1, le=20),
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    pref = current_user.preferences if current_user else None
    engine = RecommendationEngine(db)
    return engine.get_recommendations(
        user_preference=pref,
        cuisine_filter=cuisine,
        novelty_filter=novelty,
        limit=limit
    )

@router.post("/feedback")
def submit_recommendation_feedback(
    feedback: RecommendationFeedbackRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    rating = UserRating(
        user_id=current_user.id,
        score=feedback.score,
        comment=f"Feedback for {feedback.combination_name}: {feedback.comment or ''}",
        taste_feedback={"liked": feedback.liked, "ingredients": feedback.ingredients},
        would_make_again=feedback.liked
    )
    db.add(rating)
    db.commit()
    return {
        "status": "success",
        "message": f"Thank you! Your feedback for '{feedback.combination_name}' has been recorded and will refine future recommendations."
    }
