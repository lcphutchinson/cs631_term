from sqlalchemy import insert
from sqlalchemy.orm import Session

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

def load_demo_data():
    client = DatabaseClient()
    client.model_base.metadata.create_all(bind=client.engine)
    with client.session_agent() as db:
        employees = [
            {"active": True,"hourly": False,"f_name": "John","m_name": "A","l_name": "Smith","salary": 72000.00,"street": "123 Maple St","city": "Springfield","state": "IL","zip": "62701"
            },{"active": True,"hourly": True,"f_name": "Emily","m_name": None,"l_name": "Carter","salary": 22.50,"street": "456 Oak Ave","city": "Madison","state": "WI","zip": "53703"
            },{"active": True,"hourly": False,"f_name": "Michael","m_name": "J","l_name": "Brown","salary": 88000.00,"street": "789 Pine Rd","city": "Columbus","state": "OH","zip": "43215"
            },{"active": False,"hourly": True,"f_name": "Sarah","m_name": None,"l_name": "Nguyen","salary": 19.75,"street": "321 Birch Ln","city": "Portland","state": "OR","zip": "97205"
            },{"active": True,"hourly": False,"f_name": "David","m_name": "R","l_name": "Wilson","salary": 95000.00,"street": "654 Cedar Blvd","city": "Austin","state": "TX","zip": "78701"
            },{"active": True,"hourly": True,"f_name": "Laura","m_name": "M","l_name": "Hernandez","salary": 24.00,"street": "987 Elm St","city": "San Diego","state": "CA","zip": "92101"
            },{"active": True,"hourly": False,"f_name": "Brian","m_name": None,"l_name": "O'Connor","salary": 68000.00,"street": "111 Willow Way","city": "Albany","state": "NY","zip": "12207"
            },{"active": False,"hourly": False,"f_name": "Angela","m_name": "T","l_name": "Brooks","salary": 54000.00,"street": "222 Aspen Ct","city": "Boulder","state": "CO","zip": "80302"
            },{"active": True,"hourly": True,"f_name": "Kevin","m_name": None,"l_name": "Patel","salary": 21.25,"street": "333 Spruce Dr","city": "Edison","state": "NJ","zip": "08817"
            },{"active": True,"hourly": False,"f_name": "Rachel","m_name": "L","l_name": "Adams","salary": 81000.00,"street": "444 Poplar St","city": "Nashville","state": "TN","zip": "37219"
            },{"active": True,"hourly": True,"f_name": "Thomas","m_name": "E","l_name": "King","salary": 26.75,"street": "555 Hickory Rd","city": "Lexington","state": "KY","zip": "40507"
            },{"active": False,"hourly": False,"f_name": "Natalie","m_name": None,"l_name": "Foster","salary": 60000.00,"street": "666 Magnolia Ave","city": "Savannah","state": "GA","zip": "31401"}
        ]
        buildings = [
            {"name":"The Great Hall", "acq_type":"GRANT", "expense":400000},
            {"name":"The Quad", "acq_type":"LEASE", "expense":230000},
            {"name":"Auditorium", "acq_type":"PURCHASE", "expense":800000}
        ]
        db.execute(insert(Employee), employees)
        db.execute(insert(Building), buildings)
        db.commit()

        divisions = [
            {"active": True,"name":"Ops", "head":3, "budget":100000},
            {"active": True,"name":"R&D", "head":5, "budget":200000},
            {"active": False,"name":"Facilities", "head":8, "budget":0}
        ]
        db.execute(insert(Division), divisions)
        db.commit()

        departments = [
            {"active": True, "name":"Avionics","div":"Ops","head": 1,"budget":300000},
            {"active": True, "name":"Signals","div":"R&D","head": 4,"budget":200000},
            {"active": True, "name":"Machining","div":"Ops","head": 9,"budget":250000},
            {"active": True, "name":"Cyber","div":"Ops","head": 10,"budget":200000},
            {"active": False, "name":"Computing","div":"Facilities","head": 11,"budget":0}
        ]
        db.execute(insert(Department), departments)
        db.commit()
    
        rooms = [
            {"building":"The Great Hall","dept":1,"area":200},
            {"building":"The Quad","dept":2,"area":140},
            {"building":"The Quad","dept":3,"area":180},
            {"building":"The Great Hall","dept":2,"area":155},
            {"building":"Auditorium","dept":4,"area":255},
            {"building":"Auditorium","dept":3,"area":400},
            {"building":"The Great Hall","dept":4,"area":420},
            {"building":"The Quad","dept":3,"area":300},
            {"building":"The Quad","dept":1,"area":310},
            {"building":"The Great Hall","dept":1,"area":260},
            {"building":"Auditorium","dept":2,"area":280}
        ]
        projects = [
            {"active":True,"name":"Build A","manager":10,"budget":10000},
            {"active":True,"name":"Build B","manager":1,"budget":15000},
            {"active":False,"name":"Receiver","manager":3,"budget":0},
            {"active":True,"name":"Defense System","manager":9,"budget":20000},
            {"active":True,"name":"Neural Network","manager":6,"budget":14000},
            {"active":False,"name":"Web Crawler","manager":2,"budget":18000}
        ]
        db.execute(insert(Room), rooms)
        db.execute(insert(Project), projects)
        db.commit()
        
        offices = [
            {"employee":2,"room":2,"phone":"856-234-5464"},
            {"employee":3,"room":3,"phone":"345-675-7867"},
            {"employee":4,"room":2,"phone":"213-535-7676"},
            {"employee":5,"room":6,"phone":"234-546-6578"},
            {"employee":6,"room":6,"phone":"345-767-7876"},
            {"employee":7,"room":5,"phone":"231-896-0054"},
            {"employee":8,"room":4,"phone":"233-567-5655"},
            {"employee":9,"room":1,"phone":"231-234-4009"},
        ]

        milestones = [
            {"project":1,"complete":False,"description":"Coming Soon"},
            {"project":4,"complete":False,"description":"Coming Soon"},
            {"project":5,"complete":False,"description":"Coming Soon"},
            {"project":5,"complete":False,"description":"Coming Soon"},
            {"project":3,"complete":False,"description":"Coming Soon"},
            {"project":2,"complete":False,"description":"Coming Soon"},
            {"project":2,"complete":False,"description":"Coming Soon"},
            {"project":2,"complete":False,"description":"Coming Soon"},
            {"project":1,"complete":False,"description":"Coming Soon"}
        ]
        assignments = [
            {"employee":1,"project":2},
            {"employee":3,"project":2},
            {"employee":2,"project":3},
            {"employee":4,"project":3},
            {"employee":5,"project":3},
            {"employee":6,"project":1},
            {"employee":7,"project":1},
            {"employee":8,"project":5}
        ]
        dept_emp = [
            {"department":1,"employee":1},
            {"department":2,"employee":2},
            {"department":3,"employee":3},
            {"department":5,"employee":4},
            {"department":4,"employee":5},
            {"department":4,"employee":6}
        ]
        consultants = [
            {"division":"Ops","employee":7},
            {"division":"Ops","employee":8},
            {"division":"R&D","employee":9},
        ]
        db.execute(insert(Office), offices)
        db.execute(insert(Milestone), milestones)
        db.execute(insert(ProjectAssignment), assignments)
        db.execute(insert(DepartmentEmployee), dept_emp)
        db.execute(insert(Consultant), consultants)
        db.commit()
