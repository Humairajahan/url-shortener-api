from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    baseurl: HttpUrl = "http://google.com"
    longurl: HttpUrl = "https://pythonprogramminglanguage.com/randon-numbers"
