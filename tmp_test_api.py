from app import app

with app.test_client() as client:
    resp = client.get('/api/symptoms')
    print('symptoms', resp.status_code, len(resp.get_json().get('symptoms', [])))
    resp2 = client.post('/api/predict', json={'symptoms': ['fever', 'cough']})
    print('predict', resp2.status_code, resp2.get_json())
