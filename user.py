from pydantic import BaseModel
from enum import Enum
from fastapi import Query

#class Query setup regular expressions for example for checking email format
#class Role has enum- means it will allow only paramentres defined inside: admin or personal
class Role(Enum):
    admin = "admin"
    personal = "personal"

class User (BaseModel):
    name: str
    password: str
    # ... means that this paramentre have to be.
    # If you don't need it you can put None and then you can delete it from the body
    mail: str = Query(..., regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
    role: Role