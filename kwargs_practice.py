def update_user_profile(*, current_profile: dict, **kwargs) -> tuple[dict, int]:
    """Update user profile and return number of changes made"""
    number_of_changes = 0
    for key, value in kwargs.items():
        if key in current_profile:
            if current_profile[key] != value:
                current_profile[key] = value
                number_of_changes += 1
        else:
            current_profile[key] = value
            number_of_changes += 1
    return current_profile, number_of_changes
