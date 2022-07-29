cpf_existing = '98684577420'
cpf_non_existing = '98684577429'


def test_find_by_cpf_should_return_contact_when_cpf_exists(client):
    response = client.get(f'/contacts/{cpf_existing}')

    assert response.status_code == 200


def test_find_by_cpf_should_return_not_found_when_cpf_does_not_exists(client):
    response = client.get(f'/contacts/{cpf_non_existing}')

    assert response.json.get('message') == 'Recurso Sem dados.'
