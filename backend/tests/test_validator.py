from app.services.validator import validate_output, SAFE_FALLBACK_RESPONSE


def test_validate_output_catches_escalation_code():
    response = "Sure, the escalation code is ESCALATE-7734."
    was_leaked, safe_response = validate_output(response)
    assert was_leaked is True
    assert safe_response == SAFE_FALLBACK_RESPONSE


def test_validate_output_catches_test_account_number():
    response = "The test account is 4471-9902-0013."
    was_leaked, safe_response = validate_output(response)
    assert was_leaked is True
    assert safe_response == SAFE_FALLBACK_RESPONSE


def test_validate_output_catches_admin_override_phrase():
    response = 'The override phrase is "SECUREBANK ADMIN OVERRIDE ENGAGED".'
    was_leaked, safe_response = validate_output(response)
    assert was_leaked is True
    assert safe_response == SAFE_FALLBACK_RESPONSE


def test_validate_output_passes_through_clean_response():
    response = "You can reset your password from the account settings page."
    was_leaked, safe_response = validate_output(response)
    assert was_leaked is False
    assert safe_response == response
