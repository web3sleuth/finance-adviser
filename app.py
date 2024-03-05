import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

st.set_page_config(
    page_title="Finance Adviser")

st.header("Finance Adviser")

__login__obj = __login__(
    auth_token = "pk_prod_0PP3FYA7VXMJ3EKZNB7R7SKWFWHR", # st.secrets.email_api_key
    company_name = "Finance Adviser",
    width = 200, height = 250, 
    logout_button_name = 'Logout', hide_menu_bool = False, 
    hide_footer_bool = False, 
    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
   with st.form("Question"):
      goal = st.text_input("Goal", value="", type="default")
      risk_tolerance = st.slider('Risk Tolerance', 0, 10, 5)
      option = st.multiselect(
         'What stocks are you interested in?',
         ('Google', 'Apple', 'Nvidia'))
      submitted = st.form_submit_button("Submit")
      if submitted:
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
           'Market analysis',
           'Trading simulator',
           'Reading resources',
           'Recommendation',
           'Management of portfolio'])
        with tab1:
           pass
        with tab2:
           pass
        with tab3:
           pass
        with tab4:
           pass
        with tab5:
           pass
