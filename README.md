# **Object API Project**

This is a FastAPI application that provides endpoints to manipulate
**Objects**, **Owners**, **Industries**, **Documents**, **Contracts**,
and **Statuses** related to the object management system. The project is
built to provide RESTful APIs for managing and interacting with various
entities in a system related to objects and their metadata.

## **Features**

- >**Object Management**: Manage information about objects including
  > metadata, related documents, and statuses.

- >**Owner Management**: CRUD operations for managing owners and their
  > details.

- >**Industry Data**: Access industry-specific information associated
  > with objects.

- >**Document Handling**: Manage and store documents related to objects
  > and contracts.

- >**Contract Management**: Manage contracts associated with objects and
  > owners.

- >**Status Tracking**: Track various statuses for objects and their
  > related items.

## **Requirements**

To run this project, you will need the following:

- **Python 3.7+**

- **PostgreSQL** as the database backend

- **FastAPI** for the web framework

- **SQLAlchemy** for ORM and database interaction

- **PyYAML** for loading the OpenAPI YAML specification (optional if using YAML for API documentation)

## **Getting Started**

### **1. Install the dependencies:**

>pip install -r requirements.txt

### **2. Configure the database connection:**

Update the database URL in the connection.py file to match your
PostgreSQL setup.

>DATABASE_URL = \"postgresql://user:password@localhost/db_name\"

### **3. Run the application:**

Start the FastAPI server:

>uvicorn app.main:app --reload

This will start the application on http://127.0.0.1:8000.

## **API Documentation**

Once the application is running, you can access the interactive API
documentation at:

- **Swagger UI**: http://127.0.0.1:8000/docs

- **ReDoc UI**: http://127.0.0.1:8000/redoc

The Swagger UI provides an interactive interface to test the API
endpoints, view request and response formats, and explore the API in
real-time.

## **Available Endpoints**

### **Objects**

- GET /objects/: Retrieve all objects.

- GET /objects/{object_id}/: Retrieve a specific object by ID.

- POST /objects/: Create a new object.

- PUT /objects/{object_id}/: Update an existing object by ID.

- DELETE /objects/{object_id}/: Delete an object by ID.

### **Owners**

- GET /owners/: Retrieve all owners.

- GET /owners/{owner_id}/: Retrieve a specific owner by ID.

- POST /owners/: Create a new owner.

- PUT /owners/{owner_id}/: Update an existing owner by ID.

- DELETE /owners/{owner_id}/: Delete an owner by ID.

### **Industries**

- GET /industries/: Retrieve all industries.

- GET /industries/{industry_id}/: Retrieve a specific industry by ID.

### **Documents**

- GET /documents/: Retrieve all documents.

- GET /documents/{document_id}/: Retrieve a specific document by ID.

- POST /documents/: Upload a new document.

- DELETE /documents/{document_id}/: Delete a document by ID.

### **Contracts**

- GET /contracts/: Retrieve all contracts.

- GET /contracts/{contract_id}/: Retrieve a specific contract by ID.

- POST /contracts/: Create a new contract.

- PUT /contracts/{contract_id}/: Update an existing contract by ID.

- DELETE /contracts/{contract_id}/: Delete a contract by ID.

### **Statuses**

- GET /statuses/: Retrieve all statuses.

- GET /statuses/{status_id}/: Retrieve a specific status by ID.

## **Database Schema**

This application uses **SQLAlchemy** ORM with a PostgreSQL database. The
models are:

- **Object**: Contains information about objects.

- **Owner**: Represents the owner of the object.

- **Industry**: Represents the industry associated with the object.

- **Document**: Stores documents related to objects and contracts.

- **Contract**: Contains contract information.

- **Status**: Tracks the status of an object.
