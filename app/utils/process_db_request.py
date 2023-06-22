from app.utils.db_schema import session, URLs
from fastapi.responses import JSONResponse
from fastapi import HTTPException


class DBRequest:
    def __init__(self, longurl, shortcode):
        self.longurl = longurl
        self.shortcode = shortcode

    def find_entry(self):
        url_exists = (
            session.query(URLs).filter(URLs.shortcode == self.shortcode)
        ).first()
        return url_exists

    def create_entry(self, baseurl):
        url_exists = self.find_entry()
        if url_exists:
            return JSONResponse(
                status_code=200,
                content={
                    "info": "URL processing done previously",
                    "url": url_exists.shortURL,
                },
            )
        else:
            shorturl = baseurl + "/" + self.shortcode
            new_entry = URLs(
                longURL=self.longurl, shortcode=self.shortcode, shortURL=shorturl
            )
            try:
                session.rollback()
                session.add(new_entry)
                session.commit()
                return JSONResponse(
                    status_code=201,
                    content={"info": "URL processed", "url": self.shortcode},
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=e)
