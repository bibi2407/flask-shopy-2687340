#Depedendencias de flask
from flask import Flask

#Dependencia de modelos
from flask_sqlalchemy import SQLAlchemy

#Dependencia de las migraciones
from flask_migrate import Migrate

from .mi_blueprint import mi_blueprint
from app.products import products

#Crear el objeto FLASK
app = Flask(__name__)


#Dependencia de configuración
from .config import Config

#Configuracion del objeto flask
app.config.from_object(Config)

#Vicular blueprints del proyecto
app.register_blueprint(mi_blueprint)
app.register_blueprint(products)

#Crear el objeto de modelos
db = SQLAlchemy(app)

#Crear el objeto de migracion
migrate = Migrate(app, db)

#importar los models 
from .models import Cliente, Producto, Venta, Detalle
