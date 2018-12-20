import os
from flask_swagger_ui import get_swaggerui_blueprint

swaggerui_blueprint_admin = get_swaggerui_blueprint(
    os.getenv('SWAGGER_URL'),
    os.getenv('SWAGGER_API_URL'),
    config={
        'app_name': os.getenv('APP_NAME')
    }
)


# swaggerui_blueprint_api = get_swaggerui_blueprint(
#     os.getenv('SWAGGER_URL_API'),
#     os.getenv('SWAGGER_API_URL_API'),
#     config={
#         'app_name': os.getenv('APP_NAME')+"_API"
#     }
# )
