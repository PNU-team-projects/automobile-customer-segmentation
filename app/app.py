import streamlit as st
import pickle

professions = [
    "Healthcare",
    "Engineer",
    "Lawyer",
    "Entertainment",
    "Artist",
    "Executive",
    "Doctor",
    "Homemaker",
    "Marketing"
    ]

spendingScores = ["Low",
                  "Average",
                  "High"
                  ]

categories = ["Category 1",
              "Category 2",
              "Category 3",
              "Category 4",
              "Category 5",
              "Category 6"
              ]

with open("pkl/one_hot_encoder.pkl", 'rb') as file:
    encoder = pickle.load(file)

with open("pkl/kmeans.pkl", 'rb') as file:
    kmeans = pickle.load(file)

with open("pkl/scaler.pkl", 'rb') as file:
    scaler = pickle.load(file)

class Form:
    def __init__(self):
        self.gender = st.selectbox("👫 Gender of the customer", options=["Male", "Female"])
        self.married = st.checkbox("🤵Is the customer married?👰")
        self.age = st.number_input('📅 Age of the customer', min_value=18,
                                   max_value=110,
                                   value=18, step=1)
        self.graduate = st.checkbox("📚 Is the customer a graduate?")
        self.profession = st.selectbox("👷 Proffession of the customer", options=professions)
        self.workExperience = st.number_input('📅 Work experience of the customer in years', min_value=0,
                                              max_value=110,
                                              value=0, step=1)
        self.spendingScore = st.selectbox("💸 Spending score of the customer", options=spendingScores)

        self.familyMembersNumber = st.number_input(
            '👪 Number of family members of the customer (including the customer)', min_value=1,
            max_value=20,
            value=1, step=1)

        self.category = st.selectbox('📑 Anonymized category for the customer', options=categories)

        self.submit = st.button('Categorize')


def main():
    st.title('Automobile Customer Category 🚗')

    form = Form()

    if form.submit:
        form.married = {True: 1, False: 0}[form.married]
        form.graduate = {True: 1, False: 0}[form.graduate]
        form.gender = {"Female": 1, "Male": 0}[form.gender]
        form.spendingScore = {"Low": 0, "Average": 1, "High": 2}[form.spendingScore]
        proffession_category = encoder.transform([[form.profession, form.category]]).toarray()[0]
        data = [
            *proffession_category,
            form.gender,
            form.married,
            form.age,
            form.graduate,
            form.workExperience,
            form.spendingScore,
            form.familyMembersNumber
        ]

        scaled = scaler.transform([data])
        result = kmeans.predict(scaled)


        st.header(f" Result : Cluster {result[0]} 🧾")


if __name__ == '__main__':
    main()
