import pytest

from challenge_8_Remove_Duplicates_from_a_List import remove_duplicates


def test_remove_duplicates_basic_case():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]


def test_remove_duplicates_preserves_order():
    data = [3, 1, 3, 2, 1]
    assert remove_duplicates(data) == [3, 1, 2]


def test_remove_duplicates_with_strings():
    assert remove_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]


def test_remove_duplicates_single_element():
    assert remove_duplicates([42]) == [42]


def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []


def test_remove_duplicates_returns_new_list():
    original = [1, 2, 2, 3]
    result = remove_duplicates(original)

    assert result == [1, 2, 3]
    assert result is not original


@pytest.mark.parametrize(
    "bad_input",
    [
        "abc",
        123,
        None,
        True,
        False,
        {"a": 1},
        (1, 2, 3),
    ],
)
def test_remove_duplicates_rejects_non_list_input(bad_input):
    with pytest.raises(TypeError):
        remove_duplicates(bad_input)
