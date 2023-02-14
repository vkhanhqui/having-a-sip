import unittest
from unittest.mock import mock_open, patch

from src.having_a_sip import file_utils as _file_utils


class FileUtilsTest(unittest.TestCase):
    """Implement unit tests for functions in having_a_sip.file_utils"""

    @patch("src.having_a_sip.file_utils.os.path.exists")
    @patch("src.having_a_sip.file_utils.os.makedirs")
    def test_create_nonexistent_dir(self, mock_make_dirs, mock_exists):
        """Test create_dir function. Create a nonexistent directory"""
        # Mock data
        mock_exists.return_value = False
        # Test
        _file_utils.create_dir("new_dir")
        # Assert
        mock_make_dirs.assert_called_once_with("new_dir")

    @patch("src.having_a_sip.file_utils.os.path.exists")
    @patch("src.having_a_sip.file_utils.os.makedirs")
    def test_create_existent_dir(self, mock_make_dirs, mock_exists):
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
            mock_file.assert_called_once_with(fake_file_path, "w")
            mock_file().write.assert_called_once_with(content)

    @patch("src.having_a_sip.file_utils.parse_bytes_to_str")
    def test_dump_file_bytes(self, mock_parse_bytes_to_str):
        """Test dump_file function. Dump bytes to a txt file"""
        # Mock data
        fake_file_path = "path/mock.txt"
        content_bytes = bytes("Message to write on file to be written", "utf-8")
        expect_content_bytes = content_bytes
        mock_parse_bytes_to_str.return_value = content_bytes
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
            mock_parse_bytes_to_str.assert_called_once_with(expect_content_bytes)
            mock_file.assert_called_once_with(fake_file_path, "w")
            mock_file().write.assert_called_once_with(expect_content_bytes)

    @patch("src.having_a_sip.file_utils.json.dumps")
    def test_dump_file_list(self, mock_dumps):
        """Test dump_file function. Dump list to a json file"""
        # Mock data
        fake_file_path = "path/mock.json"
        content = [{
            "test_key_1": "test_value_1",
            "test_key_2": "test_value_2",
        }]
        expect_content = """
        [{"test_key_1": "test_value_1", "test_key_2": "test_value_2"}]
        """
        mock_dumps.return_value = expect_content
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
            mock_dumps.assert_called_once_with(content, indent=4)
            mock_file.assert_called_once_with(fake_file_path, "w")
            mock_file().write.assert_called_once_with(expect_content)

    @patch("src.having_a_sip.file_utils.json.dumps")
    def test_dump_file_dict(self, mock_dumps):
        """Test dump_file function. Dump dict to a json file"""
        # Mock data
        fake_file_path = "path/mock.json"
        content = {
            "test_key_1": "test_value_1",
            "test_key_2": "test_value_2",
        }
        expect_content = """
        {"test_key_1": "test_value_1", "test_key_2": "test_value_2"}
        """
        mock_dumps.return_value = expect_content
        with patch(
            "src.having_a_sip.file_utils.open",
            mock_open()
        ) as mock_file:
        # Test
            _file_utils.dump_file(
                filename=fake_file_path,
                content=content
            )
        # Assert
            mock_dumps.assert_called_once_with(content, indent=4)
            mock_file.assert_called_once_with(fake_file_path, "w")
            mock_file().write.assert_called_once_with(expect_content)

    @patch("src.having_a_sip.file_utils.os.listdir")
    @patch("src.having_a_sip.file_utils.os.path.isfile")
    def test_get_filenames(self, mock_isfile, mock_listdir):
        """Test get_filenames function. Get list of filenames"""
        # Mock data
        fake_dirname = "fake_dirname"
        expect = ["a.json", "b.txt"]
        mock_listdir.return_value = expect
        mock_isfile.side_effect = [True, True]
        # Test
        actual = _file_utils.get_filenames(fake_dirname)
        # Assert
        self.assertEqual(expect, actual)

    @patch("src.having_a_sip.file_utils.get_filenames")
    @patch("src.having_a_sip.file_utils.read_file")
    def test_read_files(self, mock_read_file, mock_get_filenames):
        """Test read_files function. Get list of files"""
        # Mock data
        fake_dirname = "fake_dirname"
        expect = [("a.txt", "content 1"), ("b.txt", "content 2")]
        mock_get_filenames.return_value = ["a.txt", "b.txt"]
        mock_read_file.side_effect = ["content 1", "content 2"]
        # Test
        actual = _file_utils.read_files(fake_dirname)
        # Assert
        self.assertEqual(expect, actual)
