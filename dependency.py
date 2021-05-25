from jose import jwt
from jose.exceptions import JOSEError
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from config import SECRET_KEY

security = HTTPBearer()


async def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    """
        Function that is used to validate the token in the case that it requires it
        Security-wise it is garbage, but it could be improved.
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(token, key=SECRET_KEY)
        if payload["name"] != "notif.ai":
            raise JOSEError("User unauthorized")
    except JOSEError as e:  # catches any exception
        raise HTTPException(
            status_code=401,
            detail=str(e))
