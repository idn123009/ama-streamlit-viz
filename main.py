import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title='Data Visualization Activity to Streamlit')

def load_data():
    data = pd.read_csv(
        "./data.csv",
        encoding='ISO-8859-1'
    )
    return data

def visualization():
    st.markdown(
        '''
        # **Data Visualization**

        Name: JM Natividad

        USN: 22014210710

        Course Code: BSCYBS
        '''
    )
    # Load data
    data = load_data()
    df = data[data.economy == "Philippines"]
    
    st.markdown("### 1. What percentage of adults have access to financial accounts (bank or mobile money)?")
    account_counts_ph = df["account"].value_counts(normalize=True) * 100
    account_labels = ["Has an Account", "No Account"]
    fig1 = plt.figure(figsize=(6,6))
    plt.pie(account_counts_ph, labels=account_labels, autopct="%1.1f%%")
    plt.title("Financial Account Ownership in the Philippines (2021)")
    st.pyplot(fig1)
    st.markdown("In the Philippines, financial account ownership is moderate but still leaves a significant portion of the population unbanked.")
    
    st.markdown("### 2. What are the primary reasons cited for not having a financial account?")
    reasons_no_account_ph = df[["fin11a", "fin11b", "fin11c", "fin11d", "fin11e", "fin11f", "fin11g", "fin11h"]]
    reasons_labels = {
        "fin11a": "Too far",
        "fin11b": "Too expensive",
        "fin11c": "Lack of documentation",
        "fin11d": "Lack of trust",
        "fin11e": "Religious reasons",
        "fin11f": "Lack of money",
        "fin11g": "Family member has one",
        "fin11h": "No need for financial services",
    }
    reasons_counts_ph = (reasons_no_account_ph == 1).sum().rename(index=reasons_labels).sort_values(ascending=False)
    fig2 = plt.figure(figsize=(10, 6))
    sns.barplot(x=reasons_counts_ph.values, y=reasons_counts_ph.index, palette="coolwarm")
    plt.xlabel("Number of Respondents")
    plt.ylabel("Reason")
    plt.title("Reasons for Not Having a Financial Account in the Philippines")
    st.pyplot(fig2)
    st.markdown(
        '''
        Top 3 reasons:
        1. **Lack of money** – Many Filipinos feel they do not have enough income to maintain an account.
        2. **Financial services being too expensive** – Banking fees and requirements may discourage account ownership.
        3. **Too far** – People feel that distance as a barrier to having a financial account.
        '''
    )

    st.markdown("### 3. How does mobile money account ownership compare to traditional bank account ownership?")
    account_types_ph = df[["account_fin", "account_mob"]].mean() * 100
    account_types_labels = ["Bank Account", "Mobile Money Account"]
    fig3 = plt.figure(figsize=(6, 6))
    sns.barplot(x=account_types_labels, y=account_types_ph.values, palette="viridis")
    plt.ylabel("Percentage of Adults")
    plt.xlabel("Account Type")
    plt.title("Bank vs. Mobile Money Account Ownership in the Philippines (2021)")
    plt.ylim(0, 100)
    st.pyplot(fig3)
    st.markdown("Traditional bank accounts are more common than mobile money accounts, but mobile money is still a growing financial tool.")

    st.markdown("### 4. How does digital payment adoption vary across different income groups?")
    digital_payments_income_ph = df.groupby("inc_q")["anydigpayment"].mean() * 100
    fig4 = plt.figure(figsize=(8, 5))
    sns.barplot(x=digital_payments_income_ph.index, y=digital_payments_income_ph.values, palette="magma")
    plt.xlabel("Income Quintile (1=Lowest, 5=Highest)")
    plt.ylabel("Percentage Using Digital Payments")
    plt.title("Digital Payment Adoption by Income Group (Philippines)")
    plt.ylim(0, 100)
    st.pyplot(fig4)
    st.markdown("Higher-income individuals are much more likely to use digital payments compared to lower-income groups. This digital divide suggests that financial technology (fintech) services should focus on improving accessibility and affordability for lower-income Filipinos.")

    st.markdown("### 5. What are the primary sources of emergency funds?")
    emergency_funds_ph = df["fin24"].value_counts(normalize=True) * 100
    emergency_labels = {
        1: "Savings",
        2: "Family/Friends",
        3: "Work Income",
        4: "Borrowing",
        5: "Sale of Assets",
        6: "Other Sources",
        7: "Cannot Obtain",
    }
    emergency_funds_ph.index = emergency_funds_ph.index.map(emergency_labels)
    fig5 = plt.figure(figsize=(10, 6))
    sns.barplot(x=emergency_funds_ph.values, y=emergency_funds_ph.index, palette="tab10")
    plt.xlabel("Percentage of Respondents")
    plt.ylabel("Source of Emergency Funds")
    plt.title("Main Source of Emergency Funds in the Philippines")
    plt.xlim(0, 100)
    st.pyplot(fig5)
    st.markdown(
        '''
        Main sources of emergency funds:
        * **Family and friends** – Many Filipinos rely on social networks rather than personal savings.
        * **Income from work** – Some depend on their earnings to cover emergencies.
        * **Borrowing and asset sales** – Others resort to loans or selling assets when faced with financial difficulties.
        '''
    )





visualization()
