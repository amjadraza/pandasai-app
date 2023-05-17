import streamlit as st

from pandasai_app.components.faq import faq


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key
    st.session_state["api_key_configured"] = True
    print(st.session_state["api_key_configured"])
    print('API key is Configured Successfully!')


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a csv file with data📄\n"
            "3. A csv file is read as Pandas Dataframe📄\n"
            "4. Ask a question about to make dataframe conversational💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=st.session_state.get("OPENAI_API_KEY", ""),
        )

        if api_key_input:
            print(f'Entered API is {api_key_input}')
            set_openai_api_key(api_key_input)

        if not st.session_state.get("api_key_configured"):
            st.error("Please configure your OpenAI API key!")
        else:
            st.markdown("OpenAi API Key Configured!")

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖Pandasai App allows you to ask questions about your "
            "csv / dataframe and get accurate answers"
        )
        st.markdown(
            "Pandasai is in active development so is this tool."
            "You can contribute to the project on [GitHub]() "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by [DR. AMJAD RAZA](https://www.linkedin.com/in/amjadraza/)")
        st.markdown("Credits for Template [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("---")

        faq()
