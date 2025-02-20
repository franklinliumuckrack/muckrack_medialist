import pandas as pd
import re

def clean_name(name):
    """Clean and format names."""
    if pd.isna(name):
        return name
    # Remove extra spaces and capitalize
    return " ".join(str(name).strip().split()).title()

def clean_email(email):
    """Clean email addresses."""
    if pd.isna(email):
        return email

    if not '@' in email:
        return None
    # Remove unwanted characters and spaces
    email = str(email).strip()
    email = re.sub(r'[<>]', '', email)
    email = re.sub(r'/$', '', email)
    return email.lower()

def format_phone_number(phone):
    """Format phone numbers."""
    if pd.isna(phone):
        return phone
    # Remove unwanted characters except +()-. and numbers
    phone = str(phone)
    phone = re.sub(r'[^\d+\-().ext\s]', '', phone)
    return phone.strip()

def clean_twitter_handle(handle):
    """Clean Twitter handles."""
    if pd.isna(handle):
        return handle
    handle = str(handle).strip()
    # Remove URL components
    handle = re.sub(r'https?://(?:www\.)?twitter\.com/', '', handle)
    handle = re.sub(r'\?.*$', '', handle)
    # Ensure @ prefix
    if not handle.startswith('@'):
        handle = '@' + handle
    return handle

