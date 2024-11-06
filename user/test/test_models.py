"""
Test Models related to the user
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelsTests(TestCase):
    """Testing the model operations of User model"""
    def test_create_user(self):
        """Test For creating user"""
        tmp_user = {'email': "awab@gmail.com", 'password': "1234"}
        user = get_user_model().objects.\
            create_user(email=tmp_user['email'],
                        password=tmp_user['password'])
        self.assertEqual(user.email, tmp_user['email'])
        self.assertTrue(user.check_password(tmp_user['password']))

    def test_create_superuser(self):
        """Test For creating user"""
        tmp_user = {'email': "awab@gmail.com", 'password': "1234"}
        user = get_user_model().objects.\
            create_superuser(email=tmp_user['email'],
                             password=tmp_user['password'])
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_email_norm(self):
        """Test For normalizing email"""
        email = 'AWAB@GMAIL.COM'
        user = get_user_model().objects.create_user(email=email,
                                                    password="1234")
        self.assertEqual(user.email, email.lower())

    def test_empty_email(self):
        """Test for inserting empty email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email="", password="1234")

    def test_invalid_email(self):
        """Test for inserting invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email="Awabgmail.com",
                                                 password="1234")
