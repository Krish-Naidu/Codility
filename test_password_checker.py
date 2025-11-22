import pytest
from unittest.mock import patch
import io
import sys


def password_check(user_password):
    """Modified version of password_check that takes password as parameter and returns result"""
    counter = 0
    messages = []

    if len(user_password) >= 8:
        counter = counter + 1
    else:
        messages.append("password must be at least 8 characters long")

    contains_digit = False
    for character in user_password:
        if character.isdigit():
            contains_digit = True
            break

    if contains_digit == True:
        counter = counter + 1
    else:
        messages.append("password must contain digits")

    contains_upper = False
    for upper in user_password:
        if upper.isupper():
            contains_upper = True
            break

    if contains_upper == True:
        counter = counter + 1
    else:
        messages.append("password must contain uppercase letters")

    if counter == 3:
        result = "strong password"
    elif counter == 2:
        result = "medium password"
    else:
        result = "weak password"
    
    return result, messages


class TestPasswordChecker:
    """Test suite for password checker functionality"""

    def test_strong_password(self):
        """Test password that meets all criteria"""
        password = "Password123"
        result, messages = password_check(password)
        assert result == "strong password"
        assert len(messages) == 0

    def test_strong_password_long(self):
        """Test strong password with extra length"""
        password = "MySecurePassword123"
        result, messages = password_check(password)
        assert result == "strong password"
        assert len(messages) == 0

    def test_weak_password_too_short(self):
        """Test password that is too short"""
        password = "Pass1"
        result, messages = password_check(password)
        assert result == "weak password" or result == "medium password"
        assert "password must be at least 8 characters long" in messages

    def test_weak_password_no_digit(self):
        """Test password without digits"""
        password = "Password"
        result, messages = password_check(password)
        assert result == "medium password"
        assert "password must contain digits" in messages

    def test_weak_password_no_uppercase(self):
        """Test password without uppercase letters"""
        password = "password123"
        result, messages = password_check(password)
        assert result == "medium password"
        assert "password must contain uppercase letters" in messages

    def test_weak_password_only_lowercase(self):
        """Test password with only lowercase letters"""
        password = "password"
        result, messages = password_check(password)
        assert result == "weak password" or result == "medium password"
        assert len(messages) >= 2

    def test_weak_password_very_short(self):
        """Test very short password"""
        password = "P1"
        result, messages = password_check(password)
        assert result == "medium password"
        assert "password must be at least 8 characters long" in messages

    def test_medium_password_no_digit(self):
        """Test medium password missing only digits"""
        password = "Password"
        result, messages = password_check(password)
        assert result == "medium password"
        assert len(messages) == 1
        assert "password must contain digits" in messages

    def test_medium_password_no_uppercase(self):
        """Test medium password missing only uppercase"""
        password = "password123"
        result, messages = password_check(password)
        assert result == "medium password"
        assert len(messages) == 1
        assert "password must contain uppercase letters" in messages

    def test_medium_password_short_with_upper_and_digit(self):
        """Test short password with uppercase and digit"""
        password = "Pass1"
        result, messages = password_check(password)
        assert result == "medium password"
        assert len(messages) == 1
        assert "password must be at least 8 characters long" in messages

    def test_edge_case_exactly_8_chars(self):
        """Test password with exactly 8 characters"""
        password = "Pass1234"
        result, messages = password_check(password)
        assert result == "strong password"
        assert len(messages) == 0

    def test_edge_case_empty_password(self):
        """Test empty password"""
        password = ""
        result, messages = password_check(password)
        assert result == "weak password"
        assert len(messages) == 3

    def test_password_with_special_characters(self):
        """Test password with special characters"""
        password = "Pass@123!"
        result, messages = password_check(password)
        assert result == "strong password"
        assert len(messages) == 0

    def test_password_all_uppercase_with_digits(self):
        """Test password with all uppercase and digits"""
        password = "PASSWORD123"
        result, messages = password_check(password)
        assert result == "strong password"
        assert len(messages) == 0

    def test_password_multiple_digits(self):
        """Test password with multiple digits"""
        password = "Password1234567890"
        result, messages = password_check(password)
        assert result == "strong password"
        assert len(messages) == 0

    def test_password_multiple_uppercase(self):
        """Test password with multiple uppercase letters"""
        password = "PASSword123"
        result, messages = password_check(password)
        assert result == "strong password"
        assert len(messages) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
