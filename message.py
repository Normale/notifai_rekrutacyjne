from fastapi import APIRouter, Depends, HTTPException
from schemas import MessageCreate, Message
import crud
from database import get_db
from sqlalchemy.orm import Session
from dependency import has_access


router = APIRouter()


@router.post("/", response_model=Message)
async def create_message(message: MessageCreate,  db: Session = Depends(get_db), auth=Depends(has_access),):
    """
    Creates message (string with length 1(min) to 160(max). 
    """
    db_message = crud.create_message(db, message.text)
    return db_message


@router.put("/{message_nr}", response_model=Message)
async def edit_message(message_nr: int, message: MessageCreate, db: Session = Depends(get_db), auth=Depends(has_access)):
    db_message = crud.update_message(db, message_nr, message.text)
    return db_message


@router.delete("/{message_nr}")
async def delete_message(message_nr: int, db: Session = Depends(get_db), auth=Depends(has_access)):
    deleted = crud.delete_message(db, message_nr)
    if not deleted:
        raise HTTPException(
            status_code=404, detail=f"Message with id {message_nr} not found")
    return {"detail": "Message successfully deleted"}


@router.get("/{message_nr}", response_model=Message)
async def view_message(message_nr: int, db: Session = Depends(get_db)):
    msg = crud.increment_views(db, message_nr)
    if msg is None:
        raise HTTPException(
            status_code=404, detail=f"Message with id {message_nr} not found")
    return msg
