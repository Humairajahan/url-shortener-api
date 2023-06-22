from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    baseurl: HttpUrl = "http://montypy.ai"
    longurl: HttpUrl = "https://pythonprogramminglanguage.com/randon-numbers"
