"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CachedTestCase(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(6,8)

        self.assertEqual(res, 14)