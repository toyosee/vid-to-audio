from pydantic import BaseModel, HttpUrl
from typing import Optional


class ConversionResponse(BaseModel):
    success: bool
    message: str
    input_file: Optional[str] = None
    output_file: Optional[str] = None
    download_url: Optional[str] = None
    title: Optional[str] = None
    source_url: Optional[str] = None

class URLConversionRequest(BaseModel):
    url: HttpUrl