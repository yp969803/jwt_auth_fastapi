import fastapi 
from fastapi import Body, Depends, HTTPException, status, UploadFile, File, Request, Response
from sqlalchemy.orm import Session 
from typing import Dict 
from schemas.users import CreateUserSchema, UserSchema, UserLoginSchema
from db_initializer import get_db
from models import users as user_model
from schemas.users import CreateUserSchema, UserSchema
from schemas.model import QuestionSchema, LinkSchema
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
async def signup(payload: CreateUserSchema=Body(),
           session: Session= Depends(get_db)
           ):
    """Processess request to register user account."""
    print("hello")
    payload.hashed_password= user_model.User.hash_password(payload.hashed_password)
    print(payload)
    try:
        os.mkdir("c:/Users/hp/Desktop/cltrH2/transciptModel/files/"+payload.email)
        return user_db_services.create_user(session, user=payload)
    except Exception as e:
        print(e)
        return {"msg":"Some internal error occured"}
   
    
       
        
    
    
    

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
            msg = "Invalid user credentials"
        )
    
    return signJWT(payload.email)
    
    
@app.post("/protected/upload",dependencies=[Depends(JWTBearer())])
async def uploadVideos(file: UploadFile,request:Request):
  try:
    vname=request.state.email+".mp4"
    email=request.state.email
    if os.path.isfile("c:/Users/hp/Desktop/cltrH2/videoDownload/videos/"+vname):
           os.remove("c:/Users/hp/Desktop/cltrH2/videoDownload/videos/"+vname)
    if os.path.isfile("c:/Users/hp/Desktop/cltrH2/transciptModel/videos/"+email+".wav"):
           os.remove("c:/Users/hp/Desktop/cltrH2/videoDownload/videos/"+email+".wav")
    with open("./videoDownload/videos/"+vname,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    text= VideoToText(vname)
    
    name=createFileFromString(text,email)
    if name=="":
        return {"msg":"Some internal error occured"}
    return text
  except Exception as e :
      print(e)
      return {"msg":"Some internal error occured"}
      
    
    
@app.post("/protected/question",response_model=Dict,dependencies=[Depends(JWTBearer())])
async def askQuestion(payload: QuestionSchema,request:Request):
    try:
      ans= getAnswer(payload.question,request.state.email)
      print(ans)
      if(type(ans)!=str):
        return {"answer": "Unable to find the answer!"} 
      return {"answer": ans} 
    except Exception as e:
        print(e)
        return {"msg":"some error occured"}


@app.get("/protected/test",response_model=Dict,dependencies=[Depends(JWTBearer())])
async def test(request: Request):
    return {"email":request.state.email};


@app.post("/protected/link",response_model=Dict,dependencies=[Depends(JWTBearer())])
async def videoLink(payload:LinkSchema,request:Request):
    try:
       
        email=request.state.email
        vname=email+".mp4"
        if os.path.isfile("c:/Users/hp/Desktop/cltrH2/videoDownload/videos/"+vname):
           os.remove("c:/Users/hp/Desktop/cltrH2/videoDownload/videos/"+vname)
        if os.path.isfile("c:/Users/hp/Desktop/cltrH2/transciptModel/videos/"+email+".wav"):
           os.remove("c:/Users/hp/Desktop/cltrH2/videoDownload/videos/"+email+".wav")
        
        isVid,video=Download(payload.link,vname)
    
        if isVid==False:
            return {"msg":"Some internal error occured"}
        
        text= VideoToText(vname)
        print(text)
        name=createFileFromString(text,email)
        if name=="":
            return {"msg":"Some internal error occured"}
        return text
    except Exception as e :
        print(e)
        return {"msg":"Internal Server error occured"}
    
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoic0BnbWFpbC5jb20iLCJleHBpcmVzIjoxNjk4NTM3NzM3LjAyMzY2MTR9.wa-BxbAK33D9Cx99y1kIziXv1xd-sA7AIUWRqmaOuTQ
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiaEBnbWFpbC5jb20iLCJleHBpcmVzIjoxNjk4NTUxOTAzLjY5OTAwNzd9.jC-kEH5Ais4Rpvcc433cfWkGwi7r2bgCois6Rtfj2CM