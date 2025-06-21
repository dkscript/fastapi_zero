from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app



def test_read_root():
    """
    Este teste tem 3 etapas:
    1. Cria um cliente de teste para a aplicação FastAPI.
    2. Faz uma requisição GET para a rota raiz ('/').
    3. Verifica se o status da resposta é 200 OK e se o corpo da resposta contém a mensagem esperada.
    
    (AAA - Arrange, Act, Assert)
    """
    # Arrange
    client = TestClient(app)
    # Act
    response = client.get('/')
    # Assert   
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}

