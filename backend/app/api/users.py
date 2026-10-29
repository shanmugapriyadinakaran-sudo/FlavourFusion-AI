from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.entities import User, UserPreference, Prediction, SavedCombination, Recipe, UserRating
from app.schemas.all_schemas import (
    UserPreferenceResponse, UserPreferenceUpdate
)
from app.api.deps import get_current_user

router = APIRouter(prefix="/users", tags=["User Preferences & Dashboard"])

@router.get("/preferences", response_model=UserPreferenceResponse)
def get_user_preferences(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    pref = db.query(UserPreference).filter(UserPreference.user_id == current_user.id).first()
    if not pref:
        pref = UserPreference(user_id=current_user.id)
        db.add(pref)
        db.commit()
        db.refresh(pref)
    return UserPreferenceResponse.model_validate(pref)

@router.put("/preferences", response_model=UserPreferenceResponse)
def update_user_preferences(
    pref_update: UserPreferenceUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    pref = db.query(UserPreference).filter(UserPreference.user_id == current_user.id).first()
    if not pref:
        pref = UserPreference(user_id=current_user.id)
        db.add(pref)

    # Update fields
    for field, value in pref_update.model_dump().items():
        setattr(pref, field, value)

    db.commit()
    db.refresh(pref)
    return UserPreferenceResponse.model_validate(pref)

@router.get("/dashboard")
def get_user_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    saved_combos = db.query(SavedCombination).filter(SavedCombination.user_id == current_user.id).all()
    saved_recipes = db.query(Recipe).filter(Recipe.user_id == current_user.id, Recipe.is_saved == True).all()
    recent_predictions = db.query(Prediction).filter(Prediction.user_id == current_user.id).order_by(Prediction.created_at.desc()).limit(10).all()
    ratings = db.query(UserRating).filter(UserRating.user_id == current_user.id).all()

    return {
        "saved_combinations_count": len(saved_combos),
        "saved_recipes_count": len(saved_recipes),
        "total_analyses_count": len(recent_predictions),
        "ratings_count": len(ratings),
        "recent_predictions": [
            {
                "id": p.id,
                "title": p.title,
                "overall_compatibility": p.overall_compatibility,
                "personalized_match": p.personalized_match,
                "created_at": p.created_at.isoformat() if p.created_at else None
            } for p in recent_predictions
        ],
        "saved_recipes": [
            {
                "id": r.id,
                "title": r.title,
                "cuisine": r.cuisine,
                "difficulty": r.difficulty,
                "servings": r.servings
            } for r in saved_recipes
        ]
    }
