from os import getenv
from os.path import dirname, isfile, join

from dotenv import load_dotenv

# uma forma de colocar dados sensíveis para a aplicação
_ENV_FILE = join(dirname(__file__), '.env')

# existindo o arquivo faça a leitura do arquivo através da função load_dotenv
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from apps import create_app

# instancia nossa função factory
app = create_app(getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    ip = '127.0.0.1'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    # inicializa o servidor Web do Flask
    app.run(host=ip, debug=debug, port=port, use_reloader=debug)
