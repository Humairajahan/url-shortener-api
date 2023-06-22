from app.utils.db_schema import session, URLs
from fastapi.responses import Response
from fastapi import HTTPException


class DBRequest:
    def __init__(self, longurl, shorturl, shortcode):
        self.longurl = longurl
        self.shorturl = shorturl
        self.shortcode = shortcode

    def find_entry(self):
        url_exists = (
            session.query(URLs).filter(URLs.shortcode == self.shortcode)
        ).first()
        return url_exists

    def create_entry(self):
        url_exists = self.find_entry()
        if url_exists:
            return Response(
                status_code=200,
                content={
                    "info": "URL processing done previously",
                    "url": url_exists.shortURL,
                },
            )
        else:
            new_entry = URLs(longURL=self.longurl, shortURL=self.shorturl, shortcode=self.shortcode)
            try:
                session.rollback()
                session.add(new_entry)
                session.commit()
                return Response(
                    status_code=201,
                    content={"info": "URL processed", "url": self.shorturl},
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=e)
            
    def return_entry(self):
        url_exists = self.find_entry()
        if url_exists:
            return url_exists.longURL
