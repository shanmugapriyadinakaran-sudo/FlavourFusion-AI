from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.entities import UserRating, User
from app.schemas.all_schemas import RatingCreateRequest
from app.api.deps import get_current_user

router = APIRouter(prefix="/ratings", tags=["Ratings & Feedback"])

@router.post("", status_code=status.HTTP_201_CREATED)
def submit_rating(
    rating_in: RatingCreateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    rating = UserRating(
        user_id=current_user.id,
        combination_id=rating_in.combination_id,
        recipe_id=rating_in.recipe_id,
        score=rating_in.score,
        comment=rating_in.comment,
        taste_feedback=rating_in.taste_feedback,
        would_make_again=rating_in.would_make_again
    )
    db.add(rating)
    db.commit()
    db.refresh(rating)

    return {
        "id": rating.id,
        "score": rating.score,
        "comment": rating.comment,
        "message": "Thank you! Your rating has been successfully saved to refine your taste profile."
    }

@router.get("")
def get_user_ratings(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    ratings = db.query(UserRating).filter(UserRating.user_id == current_user.id).order_by(UserRating.created_at.desc()).all()
    return [
        {
            "id": r.id,
            "score": r.score,
            "comment": r.comment,
            "combination_id": r.combination_id,
            "recipe_id": r.recipe_id,
            "would_make_again": r.would_make_again,
            "created_at": r.created_at.isoformat() if r.created_at else None
        } for r in ratings
    ]
