import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def wait_until_up(timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(BASE_URL + "/")
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(1)
    return False

def test_root_responds_ok():
    # O container deve estar rodando (pipeline sobe antes dos testes)
    assert wait_until_up(), "App não subiu a tempo"
    r = requests.get(BASE_URL + "/")
    assert r.status_code == 200
    data = r.json()
    assert data.get("status") == "ok"
    assert "Hello" in data.get("message", "")
