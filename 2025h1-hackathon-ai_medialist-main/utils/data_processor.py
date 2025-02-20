import pandas as pd
from .transformers import (clean_name, clean_email, format_phone_number,
                           clean_twitter_handle)
import streamlit as st

def clean_names(df, data_mapping):
  if 'name' in data_mapping:
    name_field = data_mapping['name']
    df['last_name'] = df[name_field].apply(lambda x: x.split(' ')[-1])
    df['first_name'] = df[name_field].apply(lambda x: ' '.join(x.split(' ')[:-1]))
    last_name_field = 'last_name'
    first_name_field = 'first_name'
  else:
    last_name_field = data_mapping['last_name']
    first_name_field = data_mapping['first_name']

  df[last_name_field] = df[last_name_field].apply(clean_name)
  df[first_name_field] = df[first_name_field].apply(clean_name)
  return df
    
def clean_contacts(df, data_mapping):
  if data_mapping['email']:
    email_field = data_mapping['email']

    # Split rows with multiple emails into separate row
    email_split_dfs = []
    for _, row in df.iterrows():
        if pd.notna(row[email_field]) and ';' in str(row[email_field]):
            emails = row[email_field].split(';')
            for email in emails:
                new_row = row.copy()
                new_row[email_field] = email.strip()
                email_split_dfs.append(new_row)
        else:
            email_split_dfs.append(row)

    df = pd.DataFrame(email_split_dfs)

# Clean up any whitespace around emails
    df[email_field] = df[email_field].str.strip()

    df[email_field] = df[email_field].apply(clean_email)
  if data_mapping['phonenumber']:
    phone_field = data_mapping['phonenumber']
    df[phone_field] = df[phone_field].apply(format_phone_number)
  if data_mapping['twitter']:
    twitter_field = data_mapping['twitter']
    df[twitter_field] = df[twitter_field].apply(clean_twitter_handle)

  return df

# def clean_beats(df, data_mapping, delimiter):
#     beats_field = data_mapping['beat']
#     if beats_field is not None:
#         df['beats'] = df[beats_field].apply(lambda x: ';'.join(x.split(delimiter)))
#     return df

def create_location(df, data_mapping):
  if data_mapping['address'] is None and data_mapping['city'] is not None and data_mapping['state'] is not None:
    city_field = data_mapping['city']
    state_field = data_mapping['state']
    if data_mapping['country'] is not None:
        country_field = data_mapping['country']
        df['location'] = df[city_field] + ', ' + df[state_field] + ', ' + df[country_field]
    else:
          df[location] = df[city_field] + ', ' + df[state_field]

  return df

def format_columns(df, data_mapping):
  reversed_mapping = {}
  for key, value in data_mapping.items():
    if value is not None:
      reversed_mapping[value] = key
  reversed_mapping
  df = df.rename(columns=reversed_mapping)
  return df

def process_dataframe(df, data_mapping):
    with st.spinner("Cleaning names..."):
        df = clean_names(df, data_mapping)
    with st.spinner("Cleaning contact info..."):
        df = clean_contacts(df, data_mapping)
    with st.spinner("Cleaning addresses..."):
        df = create_location(df, data_mapping)
    with st.spinner("Updating column names..."):
        df = format_columns(df, data_mapping)

    return df
