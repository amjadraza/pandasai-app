import streamlit as st
from openai.error import OpenAIError
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from pandasai_app.components.sidebar import sidebar
from pandasai_app.utils import parse_csv


def clear_submit():
    """
    Clear the Submit Button State
    Returns:

    """
    st.session_state["submit"] = False


def run_pandasai_openaiapi(df, prompt, verbose=False):
    """
    A function to run the Query on given Pandas Dataframe
    Args:
        df: Pandas dataframe
        prompt: Query / Prompt related to data
        verbose: A parameter to show the intermediate code generation

    Returns: Response / Results

    """

    llm = OpenAI(api_token=st.session_state.get("OPENAI_API_KEY"))
    pandas_ai = PandasAI(llm, verbose=verbose)
    response = pandas_ai.run(df, prompt=prompt)

    return response


if __name__ == '__main__':

    st.set_page_config(page_title="PANDASAI APP: Generative AI with Pandas", page_icon="📖", layout="wide")
    st.header("📖 Pandasai App")

    sidebar()

    # Upload the File
    uploaded_file = st.file_uploader(
        "Upload a csv file",
        type=["csv"],
        help="CSV Files are supported as of now!",
        on_change=clear_submit,
    )

    index = None
    doc = None
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = parse_csv(uploaded_file)
            index = True
        else:
            raise ValueError("File type not supported!")
        # text = text_to_docs(doc)

    query = st.text_area("Ask a question about the dataframe/csv uploaded", on_change=clear_submit)
    with st.expander("Advanced Options"):
        _verbose = st.checkbox("Show Details About Python Code generated")
        _enforce_privacy = st.checkbox("Enforce Privacy About Personal Data")

    button = st.button("Submit")

    # On SUBMIT of the button
    if button or st.session_state.get("submit"):
        if not st.session_state.get("api_key_configured"):
            st.error("Please configure your OpenAI API key!")
        elif not index:
            st.error("Please upload a data file!")
        elif not query:
            st.error("Please enter a question!")
        else:
            st.session_state["submit"] = True
            # Output Columns
            query_col, answer_col = st.columns(2)
            # sources = search_docs(index, query)
            try:
                answer = run_pandasai_openaiapi(df=df, prompt=query, verbose=False)

                with query_col:
                    st.markdown("#### Query")
                    st.markdown(query)
                with answer_col:
                    st.markdown("#### Answer")
                    st.markdown(answer)

            except OpenAIError as e:
                st.error(e._message)
