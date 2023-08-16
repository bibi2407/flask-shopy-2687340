#dependencia para hacer un blueprints
from flask import Blueprint

#definimos paquete 'products'
products = Blueprint('products',__name__,url_prefix='/products', template_folder='templates')

from .import routes