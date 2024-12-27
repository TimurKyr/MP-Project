from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import yaml

from app.routes.object_routes import router as object_router
from app.routes.owner_routes import router as owner_router
from app.routes.industry_routes import router as industry_router
from app.routes.document_routes import router as document_router
from app.routes.contract_routes import router as contract_router
from app.routes.status_routes import router as status_router


app = FastAPI()

app.include_router(object_router, prefix="/objects", tags=["Objects"])
app.include_router(owner_router, prefix="/owners", tags=["Owners"])
app.include_router(industry_router, prefix="/industries", tags=["Industries"])
app.include_router(document_router, prefix="/documents", tags=["Documents"])
app.include_router(contract_router, prefix="/contracts", tags=["Contracts"])
app.include_router(status_router, prefix="/statuses", tags=["Statuses"])


@app.get("/")
def root():
    return {"message": "This is an API to operate with Objects"}


@app.get("/export-yaml")
def export_all():
    openapi_schema = get_openapi(title="Your API", version="1.0.0", routes=app.routes)

    with open("openapi_schema.yaml", "w") as yaml_file:
        yaml.dump(openapi_schema, yaml_file, sort_keys=False)
