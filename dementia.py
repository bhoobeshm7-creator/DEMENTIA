import streamlit as st

st.set_page_config(page_title="Dementia Screening App")

st.title("🧠 Dementia Early Screening")

st.page_link("pages/01_clinical_test.py", label="📋 Clinical Dementia Test")
st.page_link("pages/02_auditory_test.py", label="🔊 Auditory Response Test")
st.page_link("pages/03_reaction_time_test.py", label="⚡ Reaction Time Test")
st.page_link("pages/04_memory_test.py", label="🧠 Memory Recall Test")
st.page_link("pages/05_final_page.py", label="📄 View Final Report")
