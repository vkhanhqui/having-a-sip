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
        mock_file_content = """Mock .txt file"""
        fake_file_path = "path/mock.txt"
        expected = mock_file_content
        # Test
        with patch(
            "src.having_a_sip.file_utils.open".format(__name__),
            new=mock_open(read_data=mock_file_content)
        ) as mock_file:
            actual = _file_utils.read_file(fake_file_path)
            mock_file.assert_called_once_with(fake_file_path, "r")
        # Assert
        self.assertEqual(expected, actual)

    def test_read_json_file(self):
        """Test read_file function. Read a json file"""
        # Mock data
        mock_file_content = """
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
            new=mock_open(read_data=mock_file_content)
        ) as mock_file:
            actual = _file_utils.read_file(
                filename=fake_file_path,
                is_json=True
            )
            mock_file.assert_called_once_with(fake_file_path, "r")
        # Assert
        self.assertEqual(expected, actual)

    def test_parse_bytes_to_str(self):
        """Test parse_bytes_to_str function. Parse bytes instance to string"""
        # Mock data
        mock_bytes = bytes("mock bytes", "utf-8")
        expected = "mock bytes"
        # Test
        actual = _file_utils.parse_bytes_to_str(
            any_bytes=mock_bytes,
        )
        # Assert
        self.assertEqual(expected, actual)

    def test_dump_file_str(self):
        """Test dump_file function. Dump string to a txt file"""
        # Mock data
        fake_file_path = "path/mock.txt"
        content = "Message to write on file to be written"
        # Test
        with patch(
            "src.having_a_sip.file_utils.open",
            mock_open()
        ) as mock_file:
            _file_utils.dump_file(
                filename=fake_file_path,
                content=content
            )
        # Assert
            # assert if opened file on write mode "w"
            mock_file.assert_called_once_with(fake_file_path, "w")
            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file
            mock_file().write.assert_called_once_with(content)

    @patch("src.having_a_sip.file_utils.parse_bytes_to_str")
    def test_dump_file_bytes(self, parse_bytes_to_str):
        """Test dump_file function. Dump bytes to a txt file"""
        # Mock data
        fake_file_path = "path/mock.txt"
        content_bytes = bytes("Message to write on file to be written", "utf-8")
        expect_content_bytes = content_bytes
        parse_bytes_to_str.return_value = content_bytes
        # Test
        with patch(
            "src.having_a_sip.file_utils.open",
            mock_open()
        ) as mock_file:
            _file_utils.dump_file(
                filename=fake_file_path,
                content=content_bytes
            )
        # Assert
            parse_bytes_to_str.assert_called_once_with(expect_content_bytes)
            # assert if opened file on write mode "w"
            mock_file.assert_called_once_with(fake_file_path, "w")
            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file
            mock_file().write.assert_called_once_with(expect_content_bytes)
