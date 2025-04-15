import unittest
from myapp.database import Database
from myapp.user_service import UserService

class TestUserServiceIntegration(unittest.TestCase):
    def setUp(self):
        self.db = Database()  # Real database (not a mock)
        self.user_service = UserService(self.db)

    def test_user_registration_and_retrieval(self):
        # Test interaction between UserService and Database
        self.user_service.register_user(1, "Alice")
        user_name = self.user_service.get_user_name(1)
        self.assertEqual(user_name, "Alice")

    def tearDown(self):
        # Clean up if needed
        pass

if __name__ == "__main__":
    unittest.main()