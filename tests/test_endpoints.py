import json

# cant get db to run during

def test_doc_post(client):
    data = {"tags": ["travel", "vacation"], "text": "my text", "authorIds": [1, 5]}
    response = client.post(
        "/docs",
        data=json.dumps(data),
    )

    assert json.dumps(response.json, sort_keys=True) == json.dumps(
        gen, sort_keys=True
    )

def test_api(client):
    response = client.post(
        "/docs"
    )

    assert json.dumps(response.json, sort_keys=True) == json.dumps(
        gen, sort_keys=True
    )

gen = {
    "generator": {
        "results": "SUCCESS"
    },
}
