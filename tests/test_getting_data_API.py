import json
from unittest.mock import Mock
from unittest.mock import patch

from src.getting_data_API import HH


def test_writing(tmp_path):
    file_path = tmp_path / "test_data"
    answer = HH(str(file_path))
    data = [{"id": 12345, "name": "Программист", "area": "Москва"}]
    answer.writing(data)
    assert file_path.exists()

    with open(file_path, "r", encoding="UTF8") as f:
        data_f = json.load(f)

    assert data_f == data


def test_reading(tmp_path):
    file_path = tmp_path / "test_data"
    data = [{"id": 12345, "name": "Программист", "area": "Москва"}]
    with open(file_path, "w", encoding="UTF8") as f:
        json.dump(data, f)
    answer = HH(str(file_path))

    assert answer.reading() == data


@patch("src.getting_data_API.requests.get")
def test_connect(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 12345, "name": "Программист", "area": "Москва"}
    answer = HH("my_file")
    result = answer.connect()
    assert result == {"id": 12345, "name": "Программист", "area": "Москва"}


def test_load_vacancies():
    answer = HH("my_file")
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "items": [
            {"id": 12345, "name": "Программист", "area": "Москва"},
            {"id": 67890, "name": "Разработчик", "area": "Тула"},
        ]
    }
    with patch("src.getting_data_API.requests.get", return_value=mock_response) as mock_get:
        result = answer.load_vacancies("Python")
    assert mock_get.called
    assert result[0]["id"] == 12345
    assert result[1]["name"] == "Разработчик"
