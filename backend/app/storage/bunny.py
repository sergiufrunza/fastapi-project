import aiohttp
from fastapi import UploadFile
from app.config import settings


async def upload_to_bunny(file_bytes: bytes, filename: str) -> str:
    cdn_url = f"{settings.bunny.cdn_url}/{settings.bunny.storage_zone}/test/{filename}"
    upload_url = (
        f"https://storage.bunnycdn.com/{settings.bunny.storage_zone}/test/{filename}"
    )

    headers = {
        "AccessKey": settings.bunny.api_key,
        "Content-Type": "application/octet-stream",
    }
    async with aiohttp.ClientSession() as session:
        async with session.put(
            upload_url, headers=headers, data=file_bytes
        ) as response:
            if response.status == 201:
                return cdn_url
            else:
                error_text = await response.text()
                raise Exception(f"Eroare la upload în Bunny CDN: {error_text}")
