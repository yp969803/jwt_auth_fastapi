import fastapi 

from fastapi import Body, Depends, HTTPException, status, UploadFile, File, Request, Response
from sqlalchemy.orm import Session 
from typing import Dict 
from schemas.users import CreateUserSchema, UserSchema, UserLoginSchema
from db_initializer import get_db
from models import users as user_model
from schemas.users import CreateUserSchema, UserSchema
from schemas.question import QuestionSchema
from services.db import users as user_db_services
import shutil
from api.auth.auth_handler import signJWT
from api.auth.auth_bearer import JWTBearer
from chatModel.model import getAnswer
from transciptModel.model import VideoToText
from videoDownload.video import Download
from utils.helper import createFileFromString
import os
import shutil
app=fastapi.FastAPI()




@app.post('/signup', response_model=UserSchema)
def signup(payload: CreateUserSchema=Body(),
           session: Session= Depends(get_db)
           ):
    """Processess request to register user account."""
    payload.hashed_password= user_model.User.hash_password(payload.hashed_password)
    try:
        os.mkdir("./transcriptModel/files/"+payload.email)
    except Exception:
        return {"msg":"Some internal error occured"}
        print(Exception)
        
    return user_db_services.create_user(session, user=payload)
    

@app.post("/login", response_model=Dict)
def login( payload: UserLoginSchema=Body(), session: Session=Depends(get_db)):
    """Processess users authentication and returns a token on successful authentication
    request body:

    - email: Unoque identifier for a user e.g email, phone number, name
    - password: 
    
    """
    try:
        user: user_model.User = user_db_services.get_user(session= session, email=payload.email)
        print(user)
    except:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED , detail= "Invalid user credentials")
    is_validated:bool= user.validate_password(payload.password)
    # is_validated:bool= True
    print(is_validated)
    if not is_validated:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Invalid user credentials"
        )
    
    return signJWT(payload.email)
    
    
@app.post("/protected/upload",dependencies=[Depends(JWTBearer())])
async def uploadVideos(file: UploadFile=File(...)):
    with open("./videoDownload/videos/"+file.filename,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return {"filename": "Done successfully"}
    
    
@app.post("/protected/question",response_model=Dict,dependencies=[Depends(JWTBearer())])
async def askQuestion(payload: QuestionSchema,request:Request):
    ans= getAnswer(payload.question,request.state.email)
    if(type(ans)!=str):
        return {"answer": "Unable to find the answer!"} 
    return {"answer": ans} 

@app.get("/protected/test",response_model=Dict,dependencies=[Depends(JWTBearer())])
async def test(request: Request):
    return {"email":request.state.email};

@app.get("/protected/video/{videoLink}",dependencies=[Depends(JWTBearer())])
async def videoLink(videoLink:str,request:Request):
    try:
        email=request.state.email
        isVid,video=Download(videoLink)
        if isVid==False:
            return {"msg":"Some internal error occured"}
        
        text= VideoToText(video.name)
        name=createFileFromString(text,email)
        if name=="":
            return {"msg":"Some internal error occured"}
        return text
    except Exception :
        print(Exception)
        return {"msg":"Internal Server error occured"}
    