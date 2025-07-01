from pydantic import BaseModel  
from pydantic_extra_types import Url  

class URLRequest(BaseModel):  
    url: Url  

class URLResponse(BaseModel):  
    short_url: str  
    original_url: str  
    expires_in: Optional[int] = None 