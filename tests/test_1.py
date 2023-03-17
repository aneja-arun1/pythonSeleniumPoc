import pytest
from assertpy import assert_that


@pytest.mark.smoke
def test_abc():
    abc = "123"
    assert_that(abc).is_equal_to("123")
