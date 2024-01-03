import streamlit as st
from additional_info import spendingScores,professions,categories


class Form:
    def __init__(self):
        self.gender = st.selectbox("👫 Gender of the customer",options=["Male","Female"])
        self.married = st.checkbox("🤵Is the customer married?👰")
        self.age = st.number_input('📅 Age of the customer', min_value=18,
                                       max_value=110,
                                       value=18, step=1)
        self.graduate = st.checkbox("📚 Is the customer a graduate?")
        self.profession = st.selectbox("👷 Proffession of the customer",options=professions)
        self.workExperience = st.number_input('📅 Work experience of the customer in years', min_value=0,
                                       max_value=110,
                                       value=0, step=1)
        self.spendingScore = st.selectbox("💸 Spending score of the customer",options=spendingScores)

        self.workExperience = st.number_input('👪 Number of family members of the customer (including the customer)', min_value=1,
                                       max_value=20,
                                       value=1, step=1)
        
        self.category = st.selectbox('📑 Anonymized category for the customer',options=categories)


        self.submit = st.button('Categorize')


def main():
    st.title('Automobile Customer Category 🚗')

    form = Form()

    if form.submit:
        st.subheader(f"🧾 Custromer category : {form.category} 🧾")




if __name__ == '__main__':
    main()