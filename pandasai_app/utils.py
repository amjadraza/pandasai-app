import re
from io import BytesIO
from typing import Any, Dict, List

import pandas as pd
import streamlit as st

@st.experimental_memo()
def parse_csv(file: BytesIO) -> str:
    """
    A function to read the csv File
    Args:
        file: File Location

    Returns: Pandas dataframe

    """
    df = pd.read_csv(file)

    return df


