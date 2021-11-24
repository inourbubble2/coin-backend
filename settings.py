import os

# Flask settings
FLASK_SERVER_NAME = '0.0.0.0:5000'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
if 'MODE' in os.environ and os.environ['MODE'] == 'docker':
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@coin-database:5432/coin-database'
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/coin-database'

