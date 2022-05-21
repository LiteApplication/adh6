import json

from test.integration.resource import TEST_HEADERS, base_url


def test_post_bug(client):
    body = {
        "title": "Broken API calls",
        "description": "All API calls are broken",
        "labels": [
            "backend",
            "api"
        ]
    }
    fake_response = {
        "id": "ed899a2f4b50b4370feeea94676502b42383c746",
        "short_id": "ed899a2f4b5",
        "title": "some commit message",
        "author_name": "Example User",
        "author_email": "user@example.com",
        "committer_name": "Example User",
        "committer_email": "user@example.com",
        "created_at": "2016-09-20T09:26:24.000-07:00",
        "message": "some commit message",
        "parent_ids": [
            "ae1d9fb46aa2b07ee9836d49862ec4e2c46fbbba"
        ],
        "committed_date": "2016-09-20T09:26:24.000-07:00",
        "authored_date": "2016-09-20T09:26:24.000-07:00",
        "stats": {
            "additions": 2,
            "deletions": 2,
            "total": 4
        },
        "web_url": "https://gitlab.example.com/thedude/gitlab-foss/-/commit/ed899a2f4b50b4370feeea94676502b42383c746"
    }

    res = client.post(
        f'{base_url}/bug_report/',
        data=json.dumps(body),
        content_type='application/json',
        headers=TEST_HEADERS
    )
    assert res.status_code == 204
