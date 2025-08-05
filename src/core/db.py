import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

# from src.config import settings

load_dotenv()

Base = declarative_base()

engine = create_async_engine(os.getenv("POSTGRES_URL"))

async_session = AsyncSession(engine)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)
