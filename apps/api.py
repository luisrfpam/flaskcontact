# Importamos as classes API e Resource
from flask_restful import Api, Resource, reqparse

from apps.responses import (
    resp_already_exists,
    resp_ok,
    resp_does_not_exist,
    resp_no_content,
    resp_created,
    resp_exception,
    resp_data_invalid
)
from apps.messages import MSG_NO_DATA, MSG_RESOURCE_CREATED, MSG_RESOURCE_UPDATED, MSG_RESOURCE_RETRIEVED, MSG_INVALID_DATA, MSG_FIELD_REQUIRED

# Inicializando alguns contatos
contacts = [
{
    'cpf'       : '88584577320',
    'nome'      : 'Luis Ricardo Farias Portela',
    'endereco'  : 'Rua Vicente Reis, n.504, Betania',
    'telefone'  : '92984030269',
    'email'     : 'luis@gmail.com'
},
{
    'cpf'       : '98684577420',
    'nome'      : 'Carlos Eduardo Silva',
    'endereco'  : 'Rua Odimar Santana, n.45, Armando Mendes',
    'telefone'  : '19994090268',
    'email'     : 'carlos@gmail.com'
},
{
    'cpf'       : '46574977320',
    'nome'      : 'Pedro Henrique Silvestre',
    'endereco'  : 'Rua Rio Negro, n.14, Lirio do Vale',
    'telefone'  : '17994020368',
    'email'     : 'pedro@gmail.com'
},
{
    'cpf'       : '90434277310',
    'nome'      : 'Luis Paulo Freire',
    'endereco'  : 'Rua Eduardo Ribeiro, n.104, Centro',
    'telefone'  : '51984040360',
    'email'     : 'paulo@gmail.com'
}]

# Criamos uma classe que extende de Resource
class Contact(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nome', type=str, required=True, help="Nome deve ser preenchido!")
    parser.add_argument('endereco', type=str, required=True, help="Endereço deve ser preenchido!")
    parser.add_argument('telefone', type=str, required=True, help="Telefone deve ser preenchido!")
    parser.add_argument('email', type=str, required=True, help="Email deve ser preenchido!")
    
    # Definimos a operação get do protocolo http - Retornando um Contato
    def get(self, cpf):
        contact = next(filter(lambda x: x['cpf'] == cpf, contacts), None)
        if contact is None:
            return resp_ok('Contact', MSG_NO_DATA.format('Contacts'),)            
        else:
            return resp_ok('Contact', MSG_RESOURCE_RETRIEVED.format('Contacts'), data=contact,)     

    # Definimos a operação delete do protocolo http - - Deletando um Contato
    def delete(self, cpf):
        global contacts
        contact = next(filter(lambda x: x['cpf'] == cpf, contacts), None)
        if contact is None:
            return resp_does_not_exist('Contact', "contato")            
        else:
            contacts = list(filter(lambda x: x['cpf'] != cpf, contacts))
            return resp_no_content()                             

    # Definimos a operação put do protocolo http - Atualizando um Contato
    def put(self, cpf):
        data = Contact.parser.parse_args()
        contact = next(filter(lambda x: x['cpf'] == cpf, contacts), None)
        if contact is None:
            return resp_does_not_exist('Contact', "contato")
        else:
            contact.update(data)
        return resp_ok('Contact', MSG_RESOURCE_UPDATED.format('Contacts'), data=contact,)

# Criamos uma classe que extende de Resource
class Contacts(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cpf', type=str, required=True, help="CPF deve ser preenchido!")
    parser.add_argument('nome', type=str, required=True, help="Nome deve ser preenchido!")
    parser.add_argument('endereco', type=str, required=True, help="Endereço deve ser preenchido!")
    parser.add_argument('telefone', type=str, required=True, help="Telefone deve ser preenchido!")
    parser.add_argument('email', type=str, required=True, help="Email deve ser preenchido!")
    
    # Definimos a operação post do protocolo http - Salvando um Contato
    def post(self):
        data = Contacts.parser.parse_args()
        if next(filter(lambda x: x['cpf'] == data['cpf'], contacts), None) is not None:
            return resp_already_exists('Contacts', "contato")                            
        contact = {'cpf': data['cpf'], 'nome': data['nome'], 'endereco': data['endereco'], 'telefone': data['telefone'], 'email': data['email']}
        contacts.append(contact)        
        return resp_created('Contacts', MSG_RESOURCE_CREATED.format('Contacts'),  data=contact,)
    
    # Definimos a operação get do protocolo http - Retornando todos os Contatos - Lista
    def get(self):
        if contacts is not None:
            if contacts != []:
                return resp_ok('Contacts', MSG_RESOURCE_RETRIEVED.format('Contacts'), data=contacts,)
            else:
                return resp_ok('Contacts', MSG_NO_DATA.format('Contacts'), data=None,)   
        else:
            return resp_ok('Contacts', MSG_NO_DATA.format('Contacts'), data=None,)


# Instânciamos a API do FlaskRestful
api = Api()


def configure_api(app):

    # adicionando as rotas
    api.add_resource(Contact, '/contacts/<string:cpf>')
    api.add_resource(Contacts, '/contacts')

    # inicializamos a api com as configurações do Flask vinda por parâmetros
    api.init_app(app)