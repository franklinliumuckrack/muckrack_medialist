import streamlit as st
import pandas as pd
from utils.data_processor import process_dataframe
from utils.validators import validate_required_columns
import io
from openai import OpenAI
import os
from utils.ai_agents import get_data_mapping

client = OpenAI(api_key=os.environ['OPEN_AI_API_KEY'])


def main():
    st.set_page_config(page_title="Media List Formatter", layout="wide")

    st.title("Media List Formatter")
    st.markdown("""
    Upload your media list spreadsheet to format it according to standardized rules.
    Supported formats: CSV, Excel (.xlsx, .xls)
    """)

    # File upload
    uploaded_file = st.file_uploader("Choose a file",
                                     type=['csv', 'xlsx', 'xls'])

    if uploaded_file is not None:
        try:
            # Read the file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success("File uploaded successfully!")

            # Show raw data preview
            st.subheader(f"Raw Data Preview: {uploaded_file.name}")
            st.markdown("Here's how your data looks before processing:")

            # Preview data
            st.markdown("**Loaded data:**")
            st.dataframe(df)
            # Display first 5 rows
            # st.markdown("**First 5 Rows:**")
            # st.dataframe(df.head())

            # Store dataframe in session state
            if "df" not in st.session_state or st.session_state.df is None:
                st.session_state.df = df

            # Initialize data mapping if not present in session_state
            if "data_mapping" not in st.session_state:
                with st.spinner("Evaluating data..."):
                    st.session_state.data_mapping = get_data_mapping(
                        df, client)

            # Function to update session state when the user modifies the data mapping
            def update_mapping(updated_mapping):
                st.session_state.data_mapping = updated_mapping

            # Display data mapping with a callback
            st.markdown("**Proposed Data Mapping:**")
            edited_data_mapping = st.data_editor(st.session_state.data_mapping,
                                                 key="data_mapping_editor",
                                                 use_container_width=True)

            # Store user edits in session state
            st.session_state.data_mapping = edited_data_mapping

            if st.button("Process Data"):
                processed_df = process_dataframe(st.session_state.df,
                                                 st.session_state.data_mapping)

                # Store processed data in session state
                st.session_state.processed_df = processed_df

                # Show preview
                st.subheader("Processed Data Preview")
                st.dataframe(processed_df)

            if "processed_df" in st.session_state:
                output = io.BytesIO()
                st.session_state.processed_df.to_excel(output, index=False)
                output.seek(0)
                input_file = uploaded_file.name.split('.')[0]
                output_filename = f'{input_file}_cleaned.xlsx'
                st.download_button(
                    label="Download Processed File",
                    data=output,
                    file_name=output_filename,
                    mime=
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        except Exception as e:
            st.error(f"Error processing file: {str(e)}")


if __name__ == "__main__":
    main()
