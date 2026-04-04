import streamlit as st

st.set_page_config(page_title="BharatScholar AI", page_icon="🇮🇳")
st.title("🇮🇳 BharatScholar AI (Demo Mode)")
st.info("💡 Full Gemma 4 local version requires Ollama. This demo simulates outputs for judges.")

menu = st.sidebar.selectbox("Module", ["UGC Compliance", "Fellowship Forms", "Expert Search", "Journal Validator"])

if menu == "UGC Compliance":
    st.success("✅ Gemma 4 validates coursework + publication status per UGC 2022 rules.")
    st.code("""{
  "eligible_for_pre_phd": true,
  "missing_requirements": ["Conference presentation recommended"],
  "recommendation": "Proceed with Pre-PhD presentation. Ensure 1 publication is in UGC-approved journal."
}""", language="json")
elif menu == "Fellowship Forms":
    st.success("📄 Annexure-I generated for UGC-JRF (26 days attendance)")
    st.text("[FORM PREVIEW] Scholar: ______ | Month: ______ | Supervisor Sign: ______")
elif menu == "Expert Search":
    st.success("🔍 5 IRINS-matched experts found for 'AI in Agriculture'")
    st.table({"Name": ["Dr. P. Sharma", "Dr. R. Kumar"], "Institution": ["IIT Delhi", "NIT Trichy"], "Vidwan ID": ["VID123", "VID456"]})
elif menu == "Journal Validator":
    st.warning("⚠️ UGC CARE discontinued Oct 2024. Switching to Transparent Peer Review framework.")
    st.success("✅ Compliance Score: 82% | Status: APPROVED for PhD submission")
