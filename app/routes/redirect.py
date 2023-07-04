from fastapi import APIRouter
from app.utils.process_db_request import DBRequest
from fastapi.responses import RedirectResponse


router = APIRouter()


@router.get("/{shortcode}", response_class=RedirectResponse, status_code=302)
async def redirect_to_original_url(shortcode: str):
    url = DBRequest(longurl=None, shorturl=None, shortcode=shortcode).return_entry()
    return url