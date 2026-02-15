def test_register_empresa(client):
    response = client.post("/api/v1/auth/register", json={
        "email": "empresa@test.com",
        "password": "senha123",
        "tipo": "empresa"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "empresa@test.com"
    assert data["tipo"] == "empresa"
    assert "id" in data

def test_register_freelancer(client):
    response = client.post("/api/v1/auth/register", json={
        "email": "freelancer@test.com",
        "password": "senha123",
        "tipo": "freelancer"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["tipo"] == "freelancer"

def test_register_duplicate_email(client):
    client.post("/api/v1/auth/register", json={
        "email": "duplicate@test.com",
        "password": "senha123",
        "tipo": "empresa"
    })
    response = client.post("/api/v1/auth/register", json={
        "email": "duplicate@test.com",
        "password": "senha456",
        "tipo": "freelancer"
    })
    assert response.status_code == 400
    assert "já cadastrado" in response.json()["detail"]

def test_register_invalid_tipo(client):
    response = client.post("/api/v1/auth/register", json={
        "email": "test@test.com",
        "password": "senha123",
        "tipo": "invalido"
    })
    assert response.status_code == 422

def test_login_success(client):
    client.post("/api/v1/auth/register", json={
        "email": "login@test.com",
        "password": "senha123",
        "tipo": "empresa"
    })
    
    response = client.post("/api/v1/auth/login", data={
        "username": "login@test.com",
        "password": "senha123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client):
    client.post("/api/v1/auth/register", json={
        "email": "wrong@test.com",
        "password": "senha123",
        "tipo": "empresa"
    })
    
    response = client.post("/api/v1/auth/login", data={
        "username": "wrong@test.com",
        "password": "senhaerrada"
    })
    assert response.status_code == 401

def test_login_user_not_found(client):
    response = client.post("/api/v1/auth/login", data={
        "username": "naoexiste@test.com",
        "password": "senha123"
    })
    assert response.status_code == 401
