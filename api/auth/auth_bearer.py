from typing import Optional
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.auth.auth_handler import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme =="Bearer":
                raise HTTPException(status_code=403,detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token")
            # request.state.email=decodeJWT(credentials.credentials)["user_id"]
            payload=decodeJWT(credentials.credentials)
            request.state.email=payload["user_id"]
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization")
    
    def verify_jwt(self, jwttoken:str) -> bool:
        isTokenValid: bool =False
        
        try:
            payload=decodeJWT(jwttoken)
            print(payload)
        except:
            payload=None
        if payload:
            isTokenValid=True
        return isTokenValid