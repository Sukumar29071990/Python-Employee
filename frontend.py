from fastapi import FastAPI
import uvicorn
from db import get_sql_connection
import pyodbc
from pydantic import BaseModel
from typing import List, Optional