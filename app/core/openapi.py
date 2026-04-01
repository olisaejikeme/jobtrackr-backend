from fastapi.openapi.utils import get_openapi

from configs.settings import settings

def custom_openapi(app):
    """
    Configures the OpenAPI schema for JobTrackr
    """
    def openapi():
        if app.openapi_schema:
            return app.openapi_schema

        # Generate default OpenAPI schema
        openapi_schema = get_openapi(
            title=settings.app_name,
            description="Application Job Tracking",
            version="v1",
            routes=app.routes,
            servers=[{"url": "/", "description": "Default Server Url"}],
            contact={"name": "Olisa Ejikeme",
                     "email": "olisaejikeme@gmail.com"},
            license_info={"name": "MIT License"},
            terms_of_service="Terms of service",
            tags=[],
        )

        # Ensure 'components' key exists
        if "components" not in openapi_schema:
            openapi_schema["components"] = {}

        openapi_schema["components"]["securitySchemes"] = {
            "BearerAuth": {
                "type": "http",
                "description": "JWT Authentication",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
        openapi_schema["security"] = [{"BearerAuth": []}]

        # prevent regeneration
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return openapi
