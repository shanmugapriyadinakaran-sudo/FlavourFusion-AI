from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.database.session import get_db
from app.models.entities import Ingredient, IngredientFlavorProfile, User
from app.schemas.all_schemas import (
    IngredientResponse, IngredientCreate, FlavorProfileData
)
from app.api.deps import get_current_user_optional

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])

@router.get("", response_model=List[IngredientResponse])
def get_ingredients(
    category: Optional[str] = None,
    cuisine: Optional[str] = None,
    exclude_allergen: Optional[str] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(350, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    query = db.query(Ingredient)

    if category and category.lower() != "all":
        cat_lower = category.lower().strip()
        if "veg" in cat_lower:
            query = query.filter(or_(Ingredient.category.ilike("%vegetable%"), Ingredient.category.ilike("%produce%")))
        elif "fruit" in cat_lower:
            query = query.filter(Ingredient.category.ilike("%fruit%"))
        elif "spice" in cat_lower or "herb" in cat_lower:
            query = query.filter(or_(Ingredient.category.ilike("%spice%"), Ingredient.category.ilike("%herb%")))
        elif "grain" in cat_lower or "lentil" in cat_lower or "dal" in cat_lower or "legume" in cat_lower:
            query = query.filter(or_(Ingredient.category.ilike("%grain%"), Ingredient.category.ilike("%lentil%"), Ingredient.category.ilike("%legume%"), Ingredient.category.ilike("%pasta%")))
        elif "dairy" in cat_lower or "cheese" in cat_lower:
            query = query.filter(Ingredient.category.ilike("%dairy%"))
        elif "meat" in cat_lower or "seafood" in cat_lower:
            query = query.filter(Ingredient.category.ilike("%meat%"))
        elif "sweet" in cat_lower or "dessert" in cat_lower or "baker" in cat_lower:
            query = query.filter(or_(Ingredient.category.ilike("%sweet%"), Ingredient.category.ilike("%dessert%"), Ingredient.category.ilike("%bake%")))
        elif "sauce" in cat_lower or "condiment" in cat_lower or "oil" in cat_lower:
            query = query.filter(or_(Ingredient.category.ilike("%sauce%"), Ingredient.category.ilike("%condiment%"), Ingredient.category.ilike("%pantry%")))
        else:
            query = query.filter(Ingredient.category.ilike(f"%{category}%"))

    ingredients = query.offset(skip).limit(limit).all()

    # In-memory filter for JSON arrays like cuisines / allergens
    filtered = []
    for ing in ingredients:
        if cuisine and cuisine.lower() != "all":
            if not any(cuisine.lower() in c.lower() for c in (ing.cuisines or [])):
                continue
        if exclude_allergen:
            if any(exclude_allergen.lower() in a.lower() for a in (ing.allergens or [])):
                continue
        filtered.append(ing)

    return [IngredientResponse.model_validate(i) for i in filtered]

@router.get("/search", response_model=List[IngredientResponse])
def search_ingredients(
    q: str = Query(..., min_length=1),
    limit: int = Query(15, ge=1, le=50),
    db: Session = Depends(get_db)
):
    search_term = f"%{q}%"
    results = db.query(Ingredient).filter(
        or_(
            Ingredient.name.ilike(search_term),
            Ingredient.category.ilike(search_term),
            Ingredient.description.ilike(search_term)
        )
    ).limit(limit).all()

    return [IngredientResponse.model_validate(i) for i in results]

@router.get("/{ingredient_id}", response_model=IngredientResponse)
def get_ingredient_by_id(ingredient_id: int, db: Session = Depends(get_db)):
    ing = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ing:
        raise HTTPException(status_code=404, detail="Ingredient not found.")
    return IngredientResponse.model_validate(ing)

@router.post("", response_model=IngredientResponse, status_code=status.HTTP_201_CREATED)
def create_custom_ingredient(
    ingredient_in: IngredientCreate,
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: Session = Depends(get_db)
):
    slug = ingredient_in.name.strip().lower().replace(" ", "-")
    existing = db.query(Ingredient).filter(
        or_(Ingredient.name.ilike(ingredient_in.name), Ingredient.slug == slug)
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="An ingredient with this name already exists.")

    ing = Ingredient(
        name=ingredient_in.name.strip().title(),
        slug=slug,
        category=ingredient_in.category,
        description=ingredient_in.description or f"Custom ingredient added by user.",
        default_unit=ingredient_in.default_unit,
        allergens=ingredient_in.allergens,
        cuisines=ingredient_in.cuisines,
        is_curated=False
    )
    db.add(ing)
    db.commit()
    db.refresh(ing)

    fp_in = ingredient_in.flavor_profile
    fp = IngredientFlavorProfile(
        ingredient_id=ing.id,
        sweet=fp_in.sweet if fp_in else 3.0,
        salty=fp_in.salty if fp_in else 1.0,
        sour=fp_in.sour if fp_in else 1.0,
        bitter=fp_in.bitter if fp_in else 1.0,
        umami=fp_in.umami if fp_in else 3.0,
        spicy=fp_in.spicy if fp_in else 1.0,
        intensity=fp_in.intensity if fp_in else 5.0,
        primary_aromas=fp_in.primary_aromas if fp_in else ["Fresh"],
        texture_profile=fp_in.texture_profile if fp_in else ["Tender"],
        dominant_compounds=fp_in.dominant_compounds if fp_in else []
    )
    db.add(fp)
    db.commit()
    db.refresh(ing)

    return IngredientResponse.model_validate(ing)
