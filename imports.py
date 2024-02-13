from typing import Union
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from main import user,Session,engine

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker,relationship
import os