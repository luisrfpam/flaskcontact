from flask import Flask
from config import config

# Realize a importação da função que configura a api
from .api import configure_api


def create_app(config_name):
    app = Flask('api-contacts')

    app.config.from_object(config[config_name])

    # executa a chamada da função de configuração
    configure_api(app)

    return app