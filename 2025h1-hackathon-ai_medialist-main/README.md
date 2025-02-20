# AI enabled media list import tool

## Background
Today media list imports take up much of the Editorial team's time.

The Editorial team has to handle hundreds of Media List Import requests every week

From Intercom:
* Median time to import is 17 hours, 
* 25th percentile is 3 hours
* 75th percentile is 29 hours

From Asana:
* Median time spent is 30 minutes (does not include time to set up import)
* 25th percentile is 10 minutes
* 75th percentile is 2 hours

The reason this is tedious is because we accept any format our customer provides, but need to reformat it for the Muck Rack import tool.
This involves renaming fields and cleaning columns

[Scope doc](https://docs.google.com/document/d/1WXJWZVGWwV_GCHnpP3bTAkMhImpgaMFvfwqGjwUpbYI/edit?tab=t.0)

## Solution
Much of this work could be automated.

The difficulty in automation is primarily in mapping the customer defined fields to the standard Muck Rack fields.

However, given recent developments in Large Language Models, we believe that they are capable of performing this data mapping.

This tool 
* Takes in a spreadsheet upload as input
* Passes a sample of the spreadsheet to ChatGPT 4o, which returns a structured data mapping
* Uses the data mapping and applies cleansing scripts and then 

## Technologies Used
* The boilerplate streamlit app was initialized by Replit Agent
* I then created the prompt and cleaning functions, and plugged them back into the application

## Future Improvements
* Handle multi-sheet excel files
* Handle mixed data
* Improve UX of field mapping
* LLMs are not guaranteed to output the expected structured format, so there is an opportunity to build in robustness check with an agentic loop
* The media list importer accepts the following fields which are not currently handled
  * Contact types
    * address_type
    * email_type
    * phonenumber_type
  * Status
    * is_banned
    * is_deceased
    * is_hidden
    * is_ignored_by_spam_check
    * is_retired
    * disable_fullcontact_updates
    * disable_twitter_updates
  * Muck Rack settings
    * email_hidden_by_admin
    * hide_articles
    * hide_email
    * hide_media_outlet_phone_numbers
    * hide_phone_number
    * hide_tweets
    * hide_word_cloud
    * should_appear_in_search
    * featured
    * verified
    * has_requested_removal
    * date_claimed
  * Activity notes -  requires special handling request
    * activity_note
    * activity_user_id
    * activity_date_created
  * Contact preferences notes - requires special handling request
    * contact_preferences_notes
  * Newsdesk contacts
    * newsdesk_contact
  * Generic contact - requires row by row handling
    * is_generic_contact
  * Contact form - requires row by row handling
    * contact_form
  * Requested information
    * requested_beats
    * requested_outlets
    * requested_regions
    * requested_title
  * Researched information
    * url_email_found
    * url_phonenumber_found
    * manual_covered_topics
    * has_no_known_email
    * has_no_known_phone_number
    * custom_pronouns
    * date_future_jobchange
    * date_last_jobchange
    * covered_topics
    * profile_image_from
  * Muck Rack identifiers
    * relationship_owner
    * organization
  * Others
    * covered
    * not_covered
    * date_automatic_media_outlets_checked
    * download_statuses
    * media_outlets_from
* Handling the more sophisticated cases could potentially use a human in the loop or agentic loop pattern
* Could look at other implementations, like this one from [inngest](https://www.inngest.com/blog/agentic-workflow-example?rdt_cid=5050329755514117843) [Github](https://github.com/inngest/vercel-ai-o1-preview-crm-agent)