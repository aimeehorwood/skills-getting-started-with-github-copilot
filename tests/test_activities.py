def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activities = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Soccer Team",
        "Swimming Club",
        "Drama Club",
        "Art Studio",
        "Debate Society",
        "Science Olympiad",
    }

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert set(payload.keys()) == expected_activities


def test_get_activities_contains_expected_fields(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert "participants" in payload[activity_name]
    assert "description" in payload[activity_name]
    assert "schedule" in payload[activity_name]
    assert "max_participants" in payload[activity_name]
    assert isinstance(payload[activity_name]["participants"], list)
