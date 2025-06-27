import unittest
from unittest.mock import patch, Mock
import requests
from data.api_client import fetch_crypto_data

class TestAPIClient(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": "bitcoin", "name": "Bitcoin", "price_change_percentage_24h": 1.23}]
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = fetch_crypto_data()
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0]['id'], "bitcoin")

    @patch('requests.get')
    def test_fetch_data_network_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        result = fetch_crypto_data()
        self.assertIsNone(result)

    @patch('requests.get')
    def test_fetch_data_non_200_status(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException("404 Not Found")
        mock_get.return_value = mock_response

        result = fetch_crypto_data()
        self.assertIsNone(result)

    @patch('requests.get')
    def test_fetch_data_malformed_json(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = ValueError("Malformed JSON")
        mock_get.return_value = mock_response

        try:
            result = fetch_crypto_data()
        except ValueError:
            result = None
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()