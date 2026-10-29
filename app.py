import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent

st.set_page_config(page_title="BRB Tech | Official Hub", page_icon="🔗", layout="wide")

# Hide Streamlit's own header, footer and padding so only the hub page shows
st.markdown(
    """
    <style>
      header, footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
      .stApp { background: #08090C; }
      .block-container, [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
      iframe { display: block; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


def data_uri(path: Path) -> str:
    return "data:image/svg+xml;base64," + base64.b64encode(path.read_bytes()).decode()


html = (ROOT / "index.html").read_text(encoding="utf-8")

# The page runs inside an iframe, so relative logo paths won't resolve: inline them
html = html.replace("logo/20261029_055102%20(1).svg", data_uri(ROOT / "logo" / "20261029_055102 (1).svg"))
html = html.replace("logo/20261029_055102.svg", data_uri(ROOT / "logo" / "20261029_055102.svg"))

# Links (tel:, mailto:, socials) must open outside the iframe
html = html.replace("<head>", '<head>\n  <base target="_blank">', 1)

components.html(html, height=1250, scrolling=True)
