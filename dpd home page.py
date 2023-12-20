import streamlit as st

def main():
    st.title("Homepage Redirection")

    # Constant URL for the Publications Division homepage
    homepage_url = "https://www.publicationsdivision.nic.in/"

    # Button to redirect to the Publications Division homepage
    if st.button("Go to Homepage"):
        st.components.v1.html(f'<script>window.open("{homepage_url}", "_blank");</script>', height=1)

if __name__ == "__main__":
    main()
