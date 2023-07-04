from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    baseurl: HttpUrl = "http://127.0.0.1:5000"
    longurl: HttpUrl = "https://pythonprogramminglanguage.com/randon-numbers"
