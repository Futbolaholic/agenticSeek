import unittest
from unittest.mock import AsyncMock, patch

from sources.interaction_checker import InteractionChecker

class TestInteractionChecker(unittest.IsolatedAsyncioTestCase):
    async def test_check_no_items(self):
        checker = InteractionChecker()
        result = await checker.check([])
        self.assertEqual(result, {'interactions': []})

    async def test_check_api(self):
        checker = InteractionChecker()
        with patch('httpx.AsyncClient.get', new_callable=AsyncMock) as mock_get:
            mock_get.return_value.json.side_effect = [
                {"approximateGroup": {"candidate": [{"rxcui": "1"}]}},
                {"fullInteractionTypeGroup": ["data"]}
            ]
            result = await checker.check(['aspirin'])
            self.assertEqual(result, ["data"])

if __name__ == '__main__':
    unittest.main()
