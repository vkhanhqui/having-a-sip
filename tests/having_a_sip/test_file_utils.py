import unittest
from unittest.mock import mock_open, patch

from src.having_a_sip import file_utils as _file_utils


class FileUtilsTest(unittest.TestCase):

    def test_read_txt_file(self):
        """Test having_a_sip.file_utils.read_file function. Read a txt file"""
        # Mock data
        file_content_mock = """Mock .txt file"""
        fake_file_path = "path/mock.txt"
        expected = file_content_mock
        # Test
        with patch(
            "src.having_a_sip.file_utils.open".format(__name__),
            new=mock_open(read_data=file_content_mock)
        ) as _file:
            actual = _file_utils.read_file(fake_file_path)
            _file.assert_called_once_with(fake_file_path, "r")
        # Assert
        self.assertEqual(expected, actual)

    def test_read_json_file(self):
        """Test having_a_sip.file_utils.read_file function. Read a json file"""
        # Mock data
        file_content_mock = """
        [{"test_key_1": "test_value_1", "test_key_2": "test_value_2"}]
        """
        fake_file_path = "path/mock.json"
        expected = [{
            "test_key_1": "test_value_1",
            "test_key_2": "test_value_2",
        }]
        # Test
        with patch(
            "src.having_a_sip.file_utils.open".format(__name__),
            new=mock_open(read_data=file_content_mock)
        ) as _file:
            actual = _file_utils.read_file(
                filename=fake_file_path,
                is_json=True
            )
            _file.assert_called_once_with(fake_file_path, "r")
        # Assert
        self.assertEqual(expected, actual)
