from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.entities import (
    Prediction, PredictionIngredient, SavedCombination, User, UserPreference
)
from app.schemas.all_schemas import (
    CombinationAnalyzeRequest, CombinationAnalyzeResponse,
    CombinationSaveRequest, SavedCombinationResponse
)
from app.services.flavor_engine import FlavorEngine
from app.api.deps import get_current_user_optional, get_current_user

router = APIRouter(prefix="/combinations", tags=["Flavor Combinations"])

@router.post("/analyze", response_model=CombinationAnalyzeResponse)
def analyze_combination(
    request: CombinationAnalyzeRequest,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    if not request.ingredients or len(request.ingredients) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one ingredient must be provided."
        )

    user_pref = None
    if current_user and current_user.preferences:
        user_pref = current_user.preferences

    engine = FlavorEngine(db)
    try:
        response = engine.analyze_combination(
            ingredients_input=request.ingredients,
            user_preference=user_pref,
            title=request.title
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    # Persist the prediction record
    pred = Prediction(
        user_id=current_user.id if current_user else None,
        title=response.title,
        overall_compatibility=response.overall_compatibility,
        personalized_match=response.personalized_match,
        taste_profile=response.taste_profile,
        aroma_profile=response.aroma_profile,
        texture_profile=response.texture_profile,
        interaction_notes=response.interaction_notes,
        flavor_conflicts=response.flavor_conflicts,
        suggested_ratios=[r.model_dump() for r in response.suggested_ratios],
        complementary_suggestions=response.complementary_suggestions,
        evidence_quality=response.evidence_quality,
        uncertainty_score=response.uncertainty_score,
        tastes_like=response.tastes_like,
        tastes_like_explanation=response.tastes_like_explanation,
        vibe_check=response.vibe_check,
        shared_molecules=response.shared_molecules,
        shared_molecule_count=response.shared_molecule_count,
        molecular_taste_synthesis=response.molecular_taste_synthesis,
        possible_dishes=[d.model_dump() for d in response.possible_dishes]
    )
    db.add(pred)
    db.commit()
    db.refresh(pred)

    # Persist ingredients used
    for ing in request.ingredients:
        pi = PredictionIngredient(
            prediction_id=pred.id,
            ingredient_name=ing.name.strip().title(),
            quantity=ing.quantity,
            unit=ing.unit,
            preparation_method=ing.preparation_method or "Raw"
        )
        db.add(pi)
    db.commit()

    response.id = pred.id
    return response

@router.get("/{prediction_id}", response_model=CombinationAnalyzeResponse)
def get_combination_analysis(prediction_id: int, db: Session = Depends(get_db)):
    pred = db.query(Prediction).filter(Prediction.id == prediction_id).first()
    if not pred:
        raise HTTPException(status_code=404, detail="Prediction analysis not found.")

    # Reconstruct ratio models
    ratio_models = [r if isinstance(r, dict) else {} for r in (pred.suggested_ratios or [])]
    dish_models = [d if isinstance(d, dict) else {} for d in (pred.possible_dishes or [])]

    return CombinationAnalyzeResponse(
        id=pred.id,
        title=pred.title,
        overall_compatibility=pred.overall_compatibility,
        personalized_match=pred.personalized_match,
        taste_profile=pred.taste_profile,
        aroma_profile=pred.aroma_profile,
        texture_profile=pred.texture_profile,
        interaction_notes=pred.interaction_notes or [],
        pairwise_matrix=[],
        flavor_conflicts=pred.flavor_conflicts or [],
        suggested_ratios=ratio_models,
        complementary_suggestions=pred.complementary_suggestions or [],
        evidence_quality=pred.evidence_quality,
        uncertainty_score=pred.uncertainty_score,
        explanation=f"Persisted analysis record for {pred.title}.",
        tastes_like=pred.tastes_like,
        tastes_like_explanation=pred.tastes_like_explanation,
        vibe_check=pred.vibe_check or "✨ Chef's Kiss",
        shared_molecules=pred.shared_molecules or [],
        shared_molecule_count=pred.shared_molecule_count or 0,
        molecular_taste_synthesis=pred.molecular_taste_synthesis or "",
        possible_dishes=dish_models
    )

@router.post("/save", response_model=SavedCombinationResponse)
def save_combination(
    request: CombinationSaveRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    pred = db.query(Prediction).filter(Prediction.id == request.prediction_id).first()
    if not pred:
        raise HTTPException(status_code=404, detail="Prediction not found.")

    existing = db.query(SavedCombination).filter(
        SavedCombination.user_id == current_user.id,
        SavedCombination.prediction_id == request.prediction_id
    ).first()

    if existing:
        return SavedCombinationResponse(
            id=existing.id,
            prediction_id=existing.prediction_id,
            custom_title=existing.custom_title,
            notes=existing.notes,
            tags=existing.tags or []
        )

    saved = SavedCombination(
        user_id=current_user.id,
        prediction_id=pred.id,
        custom_title=request.custom_title or pred.title,
        notes=request.notes,
        tags=request.tags or []
    )
    db.add(saved)
    db.commit()
    db.refresh(saved)

    return SavedCombinationResponse(
        id=saved.id,
        prediction_id=saved.prediction_id,
        custom_title=saved.custom_title,
        notes=saved.notes,
        tags=saved.tags or []
    )

@router.get("/user/saved", response_model=List[SavedCombinationResponse])
def get_saved_combinations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    saved_list = db.query(SavedCombination).filter(SavedCombination.user_id == current_user.id).all()
    results = []
    for s in saved_list:
        results.append(
            SavedCombinationResponse(
                id=s.id,
                prediction_id=s.prediction_id,
                custom_title=s.custom_title,
                notes=s.notes,
                tags=s.tags or []
            )
        )
    return results

@router.delete("/user/saved/{saved_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_saved_combination(
    saved_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    saved = db.query(SavedCombination).filter(
        SavedCombination.id == saved_id,
        SavedCombination.user_id == current_user.id
    ).first()

    if not saved:
        raise HTTPException(status_code=404, detail="Saved combination not found.")

    db.delete(saved)
    db.commit()
    return None
