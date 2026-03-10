import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASELINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory data between tests to keep tests isolated."""
    activities.clear()
    activities.update(copy.deepcopy(BASELINE_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
