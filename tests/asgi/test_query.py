def test_simple_query(schema, test_client):
    response = test_client.post("/", json={"query": "{ hello }"})

    assert response.json() == {"data": {"hello": "Hello world"}}


def test_returns_errors(schema, test_client):
    response = test_client.post("/", json={"query": "{ donut }"})

    assert response.json() == {
        "data": None,
        "errors": [
            {
                "locations": [{"column": 3, "line": 1}],
                "message": "Cannot query field 'donut' on type 'Query'.",
                "path": None,
            }
        ],
    }


def test_can_pass_variables(schema, test_client):
    response = test_client.post(
        "/",
        json={
            "query": "query Hello($name: String!) { hello(name: $name) }",
            "variables": {"name": "James"},
        },
    )

    assert response.json() == {"data": {"hello": "Hello James"}}


def test_returns_errors_and_data(schema, test_client):
    response = test_client.post("/", json={"query": "{ hello, alwaysFail }"})

    assert response.status_code == 200
    assert response.json() == {
        "data": {"hello": "Hello world", "alwaysFail": None},
        "errors": [
            {
                "locations": [{"column": 10, "line": 1}],
                "message": "You are not authorized",
                "path": ["alwaysFail"],
            }
        ],
    }
