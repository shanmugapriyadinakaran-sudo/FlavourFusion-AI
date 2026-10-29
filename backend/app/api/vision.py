from fastapi import APIRouter, UploadFile, File, HTTPException, status
from app.schemas.all_schemas import VisionIdentifyResponse, VisionConfirmRequest
from app.services.vision_engine import VisionEngine
from app.core.config import settings

router = APIRouter(prefix="/vision", tags=["Computer Vision"])
vision_engine = VisionEngine(api_key=settings.GEMINI_API_KEY)

@router.post("/identify", response_model=VisionIdentifyResponse)
async def identify_ingredients(
    file: UploadFile = File(...)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file must be a valid image (JPEG, PNG, WEBP)."
        )

    # Read bytes with file size guard
    image_bytes = await file.read()
    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if len(image_bytes) > max_bytes:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Image size exceeds maximum limit of {settings.MAX_UPLOAD_SIZE_MB}MB."
        )

    # Process image with real feature model
    result = vision_engine.identify_image(image_bytes, file.filename)
    return result

@router.post("/confirm")
def confirm_ingredients(request: VisionConfirmRequest):
    return {
        "status": "success",
        "confirmed_count": len(request.confirmed_ingredients),
        "confirmed_ingredients": request.confirmed_ingredients,
        "message": f"Successfully confirmed {len(request.confirmed_ingredients)} ingredient(s). Ready for Flavor Lab analysis."
    }
