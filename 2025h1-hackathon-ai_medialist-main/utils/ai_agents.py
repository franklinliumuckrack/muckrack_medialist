import json

def get_data_mapping(df, client):
  prompt = f"""
      You are a data analyst.
      
      You are given a dataframe with the following columns:
      
      {df.columns}
      
      And a sample of the data:
      
      {df.head().to_markdown()}
      
      You are tasked with mapping the header of the data to the following schema:
      
      'first_name': __,
      'last_name': __,
      'email': __,
      'media_outlets': __,
      'title': __,
      'twitter': __,
      'bio': __,
      'blog': __,
      'bluesky': __,
      'facebook': __,
      'flickr': __,
      'foursquare': __,
      'instagram': __,
      'linkedin': __,
      'quora': __,
      'newsletter': __,
      'tumblr': __,
      'snapchat': __,
      'rss': __,
      'threads': __,
      'website': __,
      'youtube': __,
      'pronouns':__,
      'beats': __,
      'location': __,
      'phonenumber': __,
      'contact_form': __,
      'media_list_note': __,
      'address': __,
      'address2': __,
      'city': __,
      'state': __,
      'zip_code': __,
      'country': __,
      'contact_preferences_notes': __,
      
      
      If you are not sure about a field, put None.
      If names are only in one field, use name and do not include first_name and last_name.
      
      The sample data is there to help you understand the data.
      Output the mapping of the header to the schema as a JSON object without any additional text
      """
  
  response = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="gpt-4o",
  )

  data_mapping = json.loads(response.choices[0].message.content.replace("```json", "").replace("```", ""))
  return data_mapping