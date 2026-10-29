from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.entities import (
    User, Ingredient, Prediction, Recipe, UserRating, IngredientPairingEvidence
)
from app.api.deps import get_current_admin

router = APIRouter(prefix="/admin", tags=["Admin Dashboard"])

@router.get("/stats")
def get_admin_stats(
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    total_users = db.query(User).count()
    total_ingredients = db.query(Ingredient).count()
    total_predictions = db.query(Prediction).count()
    total_recipes = db.query(Recipe).count()
    total_ratings = db.query(UserRating).count()
    total_pairings = db.query(IngredientPairingEvidence).count()

    return {
        "total_users": total_users,
        "total_ingredients": total_ingredients,
        "total_predictions": total_predictions,
        "total_recipes": total_recipes,
        "total_ratings": total_ratings,
        "total_pairing_evidence": total_pairings,
        "status": "Healthy",
        "database_type": "SQLite / PostgreSQL Persistent Storage"
    }

@router.get("/feedback")
def get_all_feedback(
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    ratings = db.query(UserRating).order_by(UserRating.created_at.desc()).limit(50).all()
    return [
        {
            "id": r.id,
            "user_id": r.user_id,
            "score": r.score,
            "comment": r.comment,
            "taste_feedback": r.taste_feedback,
            "would_make_again": r.would_make_again,
            "created_at": r.created_at.isoformat() if r.created_at else None
        } for r in ratings
    ]

@router.delete("/ingredients/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient(
    ingredient_id: int,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    ing = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ing:
        raise HTTPException(status_code=404, detail="Ingredient not found.")
    db.delete(ing)
    db.commit()
    return None
