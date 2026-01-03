"""Input validation utilities for the Todo application."""


def validate_id(id_str: str) -> tuple[bool, int | None, str | None]:
    """Validate task ID input.

    Args:
        id_str: String representation of task ID

    Returns:
        Tuple of (is_valid, parsed_id, error_message)
    """
    try:
        task_id = int(id_str)
        if task_id <= 0:
            return False, None, "ID must be a positive number."
        return True, task_id, None
    except ValueError:
        return False, None, "Invalid ID. Please enter a numeric value."


def validate_title(title: str) -> tuple[bool, str, str | None]:
    """Validate and truncate task title.

    Args:
        title: Task title string

    Returns:
        Tuple of (is_valid, processed_title, warning_message)
    """
    if not title or title.strip() == "":
        return False, "", "Title cannot be empty."

    title = title.strip()
    warning = None

    if len(title) > 200:
        title = title[:200]
        warning = "Warning: Title truncated to 200 characters."

    return True, title, warning


def validate_description(description: str) -> tuple[str, str | None]:
    """Validate and truncate task description.

    Args:
        description: Task description string

    Returns:
        Tuple of (processed_description, warning_message)
    """
    description = description.strip()
    warning = None

    if len(description) > 1000:
        description = description[:1000]
        warning = "Warning: Description truncated to 1000 characters."

    return description, warning
