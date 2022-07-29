cpf_existing = '98684577420'
cpf_non_existing = '98684577429'


def test_delete_should_return_no_content_when_cpf_exists(client):
    response = client.delete(f'/contacts/{cpf_existing}')

    assert response.status_code == 204


def test_delete_should_return_not_found_when_cpf_does_not_exists(client):
    response = client.delete(f'/contacts/{cpf_non_existing}')

    assert response.status_code == 404
