from pathlib import Path
from typing import TYPE_CHECKING

import aiofiles
import fitz

if TYPE_CHECKING:
    from fastapi import UploadFile


async def pdf_to_txt(path: Path, file: "UploadFile") -> None:
    pdf_document = fitz.open(path)
    text = ""
    for page in pdf_document:
        text += page.get_text()
    async with aiofiles.open(path, "wb") as f:
        await f.write(text.encode("utf-8"))
