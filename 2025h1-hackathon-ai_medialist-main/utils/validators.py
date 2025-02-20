def validate_required_columns(df, required_columns):
    """Validate that all required columns are present in the dataframe."""
    missing_columns = [col for col in required_columns if col not in df.columns]
    return len(missing_columns) == 0, missing_columns

def validate_email(email):
    """Validate email format."""
    import re
    if pd.isna(email):
        return True
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, str(email)))

def validate_phone(phone):
    """Validate phone number format."""
    import re
    if pd.isna(phone):
        return True
    pattern = r'^\+?[\d\s\-\.()\[\]]+(?:ext\.?\s*\d+)?$'
    return bool(re.match(pattern, str(phone)))
