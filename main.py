"""FastAPI and Jinja2 App with Endpoints"""
import logging
import uvicorn

from contextlib import asynccontextmanager

from fastapi import Body, FastAPI, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import delete, inspect, join, select
from sqlalchemy.orm import Session

from typing import List

from app.db_client import DatabaseClient
from app.models.building import Building
from app.models.department import Department
from app.models.division import Division
from app.models.project import Project
from app.models.employee import Employee
from app.models.room import Room
from app.models.office import Office
from app.models.work_record import WorkRecord
from app.models.dept_emp import DepartmentEmployee
from app.models.proj_assignment import ProjectAssignment
from app.models.consultant import Consultant
from app.models.tax_record import TaxRecord
from app.models.milestone import Milestone

from app.schemas.consultant import AffiliationCreate, ConsultantCreate, ConsultantRead
from app.schemas.building import BuildingCreate, BuildingRead, BuildingUpdate
from app.schemas.department import DepartmentCreate, DepartmentRead, DepartmentUpdate
from app.schemas.dept_emp import DepartmentEmployeeCreate, DepartmentEmployeeRead
from app.schemas.division import DivisionCreate, DivisionRead, DivisionUpdate
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeRead, EmployeeVerboseRead, SafeEmployeeRead
from app.schemas.office import OfficeCreate, OfficeRead, OfficeUpdate
from app.schemas.milestone import MilestoneCreate, MilestoneUpdate, MilestoneRead
from app.schemas.project import SimpleProjectRead, ProjectCreate, ProjectRead, ProjectUpdate
from app.schemas.proj_assignment import ProjectAssignmentCreate, ProjectAssignmentRead
from app.schemas.room import RoomCreate, RoomRead, RoomUpdate
from app.schemas.tax_records import TaxRecordCreate, TaxRecordRead
from app.schemas.work_record import WorkRecordCreate, WorkRecordRead, WorkRecordUpdate


# ------------
# Setup
# ------------

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing Database")
    client = DatabaseClient()
    client.model_base.metadata.create_all(bind=client.engine)
    logger.info("Initialization Successful")
    yield

app = FastAPI(
    title="OrgDB API",
    description="API for Org database management",
    version="1.0.0",
    lifespan=lifespan
)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

DEMO = True
inspector = inspect(DatabaseClient().engine)
if DEMO and not inspector.has_table('employee'):
    from demo_data import load_demo_data
    load_demo_data()

# ------------
# Page Endpoints
# ------------

@app.get("/", response_class=HTMLResponse, tags=["web"])
def get_homepage(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/hrm", response_class=HTMLResponse, tags=["web"])
def get_hrm(request:Request):
    return templates.TemplateResponse("hrm.html", {"request": request})

@app.get("/pm", response_class=HTMLResponse, tags=["web"])
def get_pm(request:Request):
    return templates.TemplateResponse("pm.html", {"request":request})

@app.get("/hrm/emp_create", response_class=HTMLResponse, tags=["web"])
def employee_create(request:Request):
    return templates.TemplateResponse("hrm.html", {"request":request}) #PLACEHOLDER

@app.get("/hrm/emp_browse", response_class=HTMLResponse, tags=["web"])
def employee_browse(request:Request):
    return templates.TemplateResponse("employee_browse.html", {"request":request})

@app.get("/hrm/emp_detail/{emp}", response_class=HTMLResponse, tags=["web"])
def employee_detail(request:Request,
                    emp: int,
                    db: Session = Depends(DatabaseClient().get_session)):
    employee = get_verbose_employee(emp, db)
    return templates.TemplateResponse(
        "employee_detail.html", 
        {"request": request, "employee": employee}
    )

@app.get("/hrm/records_browse", response_class=HTMLResponse, tags=["web"])
def tax_record_browse(request:Request):
    return templates.TemplateResponse("hrm.html", {"request":request}) #PLACEHOLDER

@app.get("/pm/proj_create", response_class=HTMLResponse, tags=["web"])
def project_create(request:Request):
    return templates.TemplateResponse("pm.html", {"request":request}) #PLACEHOLDER

@app.get("/pm/proj_browse", response_class=HTMLResponse, tags=["web"])
def project_browse(request:Request):
    return templates.TemplateResponse("project_browse.html", {"request":request})

@app.get("/pm/records_browse", response_class=HTMLResponse, tags=["web"])
def work_record_browse(request:Request):
    return templates.TemplateResponse("pm.html", {"request":request}) #PLACEHOLDER

# ------------
# Health Endpoint
# ------------


# ------------
# Building Endpoints
# ------------


# ------------
# Department Endpoints
# ------------


# ------------
# Division Endpoints
# ------------


# ------------
# Office Endpoints
# ------------

@app.patch(
    "/api/office/create",
    status_code=status.HTTP_201_CREATED
)
def update_office(
    office: OfficeCreate,
    db: Session = Depends(DatabaseClient().get_session)):
    q = select(
        Office.employee,
        Office.room,
        Office.phone
    ).where(Office.employee == emp)
    old_office = db.execute(q).first()
    if office:
        db.delete(old_office)
    db.add(office)
    db.commit()


# ------------
# Project Endpoints
# ------------

@app.get(
    "/api/projects",
    response_model=List[SimpleProjectRead],
)
def list_projects(db: Session = Depends(DatabaseClient().get_session)):
    q = select(
        Project.num,
        Project.name,
        Project.deadline
    ).filter(Project.active == True)
    results = db.execute(q).all()
    return results

# ------------
# Work Record Endpoints
# ------------


# ------------
# Consultant Endpoints
# ------------
@app.patch(
    "/api/affiliation/create",
    status_code=status.HTTP_201_CREATED
)
def create_affiliation(
        aff: AffiliationCreate,
        db: Session = Depends(DatabaseClient().get_session)):
    old_aff = db.query(Consultant).get(aff.employee)
    if not old_aff:
        old_aff = db_query(DepartmentEmployee).get(aff.employee)
    if old_aff:
        db.delete(old_aff)
    aff_dict = aff.model_dump()
    q = insert(Consultant).values(employee=aff_dict.employee, division=aff_dict.id) \
        if 'division' in aff_dict else \
        insert(DepartmentEmployee).values(employee=aff_dict.employee, department=aff_dict.id)
    db.execute(q)
    db.commit()

    
# ------------
# Department Employee Endpoints
# ------------


# ------------
# Employee Endpoints
# ------------

@app.get(
    "/api/employee/{emp}",
    response_model=EmployeeVerboseRead,
)
def get_verbose_employee(
        emp: int,
        db: Session = Depends(DatabaseClient().get_session)):
    q = select(
        Employee.__table__.columns,
        Office.room,
        Office.phone,
        Department.name.label("dept_name"),
        Consultant.division.label("div_name"),
    ).select_from(Employee).outerjoin(
        DepartmentEmployee, Employee.num == DepartmentEmployee.employee
            ).outerjoin(Department, Department.num == DepartmentEmployee.department
                ).outerjoin(Consultant, Employee.num == Consultant.employee
                    ).outerjoin(Office, Employee.num == Office.employee
    ).where(Employee.num == emp)
    result = db.execute(q).first()
    if result._mapping.get('dept_num'):
        affiliation = {
            "aff_type": "department",
            "aff_name": result.dept_name
        }
    elif result._mapping.get('div_id'):
        affiliation = {
            "aff_type": "division",
            "aff_name": result.div_name,
        }
    else:
        affiliation = {
            "aff_type": None,
            "aff_name": None
        }
    return dict(result._mapping) | affiliation

@app.get(
    "/api/employees",
    response_model=List[SafeEmployeeRead],
)
def list_employees_safe(db: Session = Depends(DatabaseClient().get_session)):
    q = select(
        Employee.num,
        Employee.f_name,
        Employee.l_name,
        Employee.hourly,
        Employee.salary
    ).filter(Employee.active == True)
    results = db.execute(q).all()
    return results
    
@app.patch(
    "/api/employee/{emp}/edit",
    status_code=status.HTTP_204_NO_CONTENT
)
def edit_employee(
        emp: int,
        update: EmployeeUpdate,
        db: Session = Depends(DatabaseClient().get_session)):
    employee = db.query(Employee).get(emp)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee #{emp} not found"
        )
    for key, value in update.__dict__.items():
        if hasattr(employee, key) and value is not None:
            setattr(employee, key, value)
    db.commit()


# ------------
# Project Assignment Endpoints
# ------------


# ------------
# Room Endpoints
# ------------



if __name__ == "__main__":
    uvicoorn.run(app, host="127.0.0.1", port=8000, log_level="info")
