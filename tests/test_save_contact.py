def test_insert_should_return_contact_created(client):
    response = client.post(
        '/contacts',
        json={
            'cpf': '12365670900',
            'nome': 'Felipe Bastos',
            'endereco': 'Rua Central Campinas, n.01, São Paulo',
            'telefone': '19997457967',
            'email': 'felipe@gmail.com',
        },
    )

    assert response.status_code == 201
    assert response.json.get('message') == 'Recurso Contacts criado.'
    assert response.json.get('data').get('nome') == 'Felipe Bastos'
