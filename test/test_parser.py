import pytest
from app.parser import parse_command


@pytest.mark.parametrize(
    "user_input, expected_action",
    [
        ("hint", "hint"),
        ("check", "check"),
        ("quit", "quit"),
        ("A3 4", "move"),
        ("c5 clear", "clear"),
        ("J1 4", "invalid"),
        ("A10 4", "invalid"),
        ("A3 0", "invalid"),
        ("hello", "invalid"),
        ("", "invalid"),
    ],
)
def test_parse_command(user_input, expected_action):
    result = parse_command(user_input)
    assert result.action == expected_action