import streamlit as st

st.title("💡 Python موقعي الأول بـ")
st.write("!مرحباً بك في موقعي المصنوع بيدي")

# آلة حاسبة بسيطة للتوفير
saving_month = st.number_input(
    "قداه تحب تختبي كل شهر (بالدينار)؟", min_value=0
)
total_year = saving_month * 12

if st.button("احسب قداه تجمع في العام"):
    st.success(f"تجمع تقريبا: {total_year} دينار")
