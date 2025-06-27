import unittest
from unittest.mock import patch
from data.api_client import fetch_crypto_data

class TestAPIClient(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"id": "bitcoin"}]
        self.assertIsNotNone(fetch_crypto_data())

if __name__ == "__main__":
    unittest.main()