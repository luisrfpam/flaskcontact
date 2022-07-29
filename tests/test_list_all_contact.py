def test_find_all_should_page(client):
    response = client.get('/contacts')

    assert response.status_code == 200
