import pytest
import json
import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            './'
        )
    )
)
import lambda_function


@pytest.fixture()
def setup():
    print("setting up")
    return {
        "event": {
            "temp1": "test"
        },
        "expected_body": "Good Day from CloudBot!"
    }


def test_response_statuscode(setup):
    result = lambda_function.lambda_handler(setup['event'], None)
    assert result['statusCode'] == 200


def test_response_body(setup):
    result = lambda_function.lambda_handler(setup['event'], None)
    print(result['body'])
    assert result['body'] == json.dumps(
                setup['expected_body'],
                indent=4,
                sort_keys=True,
                default=str
            )
