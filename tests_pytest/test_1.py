import pytest
from django.contrib.auth.models import User

@pytest.fixture()
def create_user(db):
    user = User.objects.create_user('test_user')
    return user


def test_check_pass(create_user: User):
    create_user.set_password('1234')
    assert create_user.check_password('1234') is True
