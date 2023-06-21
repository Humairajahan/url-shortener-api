from fastapi import APIRouter
from app.utils.model import URLRequest
from app.utils.uuid_generator import short_uuid
from app.utils.process_db_request import DBRequest


router = APIRouter()


@router.post("/shortenURL")
async def shorten_url(request: URLRequest):
    shortcode = short_uuid(longurl=short_uuid(request.longurl))
    short_url = request.baseurl + "/" + shortcode
    return DBRequest(request=request, shortcode=short_url).create_entry()
