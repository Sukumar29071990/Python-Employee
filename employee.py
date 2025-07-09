from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from db import get_sql_connection
import pyodbc


app = FastAPI()

class Employee(BaseModel):
    empid : int
    empname : str
    department : str

connection = get_sql_connection()

@app.get("/")
def get_employees():  
    employees = []
    conn = pyodbc.connect(connection)
    cursor = conn.cursor()
    cursor.execute("SELECT EMPID, TRIM(EMPNAME) AS EMPNAME, TRIM(DEPARTMENT) AS DEPARTMENT FROM Employee" \
     " ORDER BY EmpID")
    for (empid, empname, department) in cursor:
        employees.append({
            "empid" : empid,
            "empname" : empname,
            "department" : department,
        })
    conn.close()
    return employees

@app.post("/addemployee/")
def insert_employee(employee : Employee):
    conn = pyodbc.connect(connection)
    cursor = conn.cursor()    
    query = (f"INSERT INTO Employee(empid,empname,department) VALUES({employee.empid},'{employee.empname}', '{employee.department}')")
    cursor.execute(query)
    conn.commit()
    conn.close()
    return cursor.rowcount

@app.put("/updateemployee/")
def update_employee(employee : Employee):
    conn = pyodbc.connect(connection)
    cursor = conn.cursor() 
    query=(f"UPDATE Employee SET EmpName='{employee.empname}', Department='{employee.department}' WHERE EmpID={employee.empid}")
    cursor.execute(query)
    conn.commit()
    conn.close()
    return cursor.rowcount

@app.delete("/employee/{empid}")
def dalete_employee(emp_id):
    conn = pyodbc.connect(connection)
    cursor = conn.cursor()
    query = (f"DELETE FROM Employee where EmpID={emp_id}")
    cursor.execute(query)
    conn.commit()
    conn.close()
    return cursor.rowcount

if __name__== '__employee__':   
  uvicorn.run(app, host="0.0.0.0", port=8000)