import unittest
from unittest.mock import mock_open, patch

from src.having_a_sip import file_utils as _file_utils


class FileUtilsTest(unittest.TestCase):
    """Implement unit tests for functions in having_a_sip.file_utils"""

    @patch("src.having_a_sip.file_utils.exists")
    @patch("src.having_a_sip.file_utils.makedirs")
    def test_create_nonexistent_dir(
        self,
        mock_make_dirs,
        mock_exists
    ):
        """Test create_dir function. Create a nonexistent directory"""
        # Mock data
        mock_exists.return_value = False
        # Test
        _file_utils.create_dir("new_dir")
        # Assert
        mock_make_dirs.assert_called_once_with("new_dir")

    @patch("src.having_a_sip.file_utils.exists")
    @patch("src.having_a_sip.file_utils.makedirs")
    def test_create_existent_dir(
        self,
        mock_make_dirs,
        mock_exists
    ):
        """Test create_dir function. Create an existent directory"""
        # Mock data
        mock_exists.return_value = True
        # Test
        _file_utils.create_dir("new_dir")
        # Assert
        mock_make_dirs.assert_not_called()

    def test_read_txt_file(self):
        """Test read_file function. Read a txt file"""
        # Mock data
        mocked_file_content = """Mock .txt file"""
        fake_file_path = "path/mock.txt"
        expected = mocked_file_content
        # Test
        with patch(
            "src.having_a_sip.file_utils.open".format(__name__),
            new=mock_open(read_data=mocked_file_content)
        ) as _file:
            actual = _file_utils.read_file(fake_file_path)
            _file.assert_called_once_with(fake_file_path, "r")
        # Assert
        self.assertEqual(expected, actual)

    def test_read_json_file(self):
        """Test read_file function. Read a json file"""
        # Mock data
        mocked_file_content = """
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
            new=mock_open(read_data=mocked_file_content)
        ) as _file:
            actual = _file_utils.read_file(
                filename=fake_file_path,
                is_json=True
            )
            _file.assert_called_once_with(fake_file_path, "r")
        # Assert
        self.assertEqual(expected, actual)

    def test_parse_bytes_to_str(self):
        """Test parse_bytes_to_str function. Parse bytes instance to string"""
        # Mock data
        mocked_bytes = bytes("mocked bytes", "utf-8")
        expected = "mocked bytes"
        # Test
        actual = _file_utils.parse_bytes_to_str(
            any_bytes=mocked_bytes,
        )
        # Assert
        self.assertEqual(expected, actual)
