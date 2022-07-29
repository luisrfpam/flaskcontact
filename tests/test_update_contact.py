cpf_existing = '88889577320'
cpf_non_existing = '98684577429'


def test_update_should_return_contact_when_cpf_exist(client):
    response = client.put(
        f'/contacts/{cpf_existing}',
        json={
            'nome': 'Luis Roberto Marinho Castro',
            'endereco': 'Rua Joaquim Marcelino, n.126, São Paulo',
            'telefone': '92984030269',
            'email': 'luis@gmail.com',
        },
    )

    assert response.status_code == 200
    assert response.json.get('message') == 'Recurso Contacts atualizado.'
    assert response.json.get('data').get('nome') == 'Luis Roberto Marinho Castro'


def test_update_should_return_not_found_when_cpf_does_not_exist(client):
    response = client.put(
        f'/contacts/{cpf_non_existing}',
        json={
            'nome': 'Luis Roberto Marinho Castro',
            'endereco': 'Rua Joaquim Marcelino, n.126, São Paulo',
            'telefone': '92984030269',
            'email': 'luis@gmail.com',
        },
    )
    assert response.status_code == 404
    assert response.json.get('message') == 'Este(a) contato não existe.'
