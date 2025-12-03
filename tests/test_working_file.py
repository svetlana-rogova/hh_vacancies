import json

import pytest

from src.working_file import WorkingDataJSON


def test_add_info(tmp_path):
    file_path = tmp_path / "test_data"
    with pytest.raises(FileNotFoundError):
        with open(file_path, "r", encoding="UTF8") as f:
            json.load(f)


def test_add_info_two(tmp_path, vacancies_one_list, vacancies_two_list):
    file_path = tmp_path / "test_data"
    file_path.write_text(json.dumps([vacancies_one_list.to_dict()]), encoding="UTF8")
    writer = WorkingDataJSON(str(file_path))
    data = vacancies_two_list
    writer.add_info(data)
    result = json.loads(file_path.read_text(encoding="UTF8"))
    assert result == [vacancies_one_list.to_dict()]


def test_add_info_three(tmp_path, vacancies_one_list, vacancies_three_list):
    file_path = tmp_path / "test_data"
    file_path.write_text(json.dumps([vacancies_one_list.to_dict()]), encoding="UTF8")
    writer = WorkingDataJSON(str(file_path))
    data = vacancies_three_list
    writer.add_info(data)
    result = json.loads(file_path.read_text(encoding="UTF8"))
    assert result == [vacancies_one_list.to_dict(), vacancies_three_list.to_dict()]


def test_get(tmp_path, vacancies, vacancies2):
    file_path = tmp_path / "test_data"
    file_path.write_text(json.dumps(vacancies, ensure_ascii=False), encoding="UTF8")
    writer = WorkingDataJSON(str(file_path))
    result = writer.get("Текст")
    expected = vacancies2
    assert result[0].to_dict() == expected[0]


def test_del_info(tmp_path, vacancies_one_list):
    file_path = tmp_path / "test_data"
    file_path.write_text(json.dumps([vacancies_one_list.to_dict()]), encoding="UTF8")
    writer = WorkingDataJSON(str(file_path))
    writer.delete_info()
    assert file_path.read_text() == ""


def test_del_vac(tmp_path, vacancies_two_list):
    file_path = tmp_path / "test_data"
    file_path.write_text(json.dumps([vacancies_two_list.to_dict()]), encoding="UTF8")
    writer = WorkingDataJSON(str(file_path))
    writer.delete_vac(123)
    assert json.loads(file_path.read_text(encoding="UTF8")) == []
