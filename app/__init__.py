#Depedendencias de flask
from flask import Flask

#Dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de las migraciones
from flask_migrate import Migrate

#Crear el objeto FLASK
app = Flask(__name__)

#Dependencia de configuración
from .config import Config

#Configuracion del objeto flask
app.config.from_object(Config)

#Crear el objeto de modelos
db = SQLAlchemy(app)

#Crear el objeto de migracion
migrate = Migrate(app, db)

#importar los models 
from .models import Cliente, Producto, Venta, Detalle
