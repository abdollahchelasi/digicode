import streamlit as st


with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

c1,c2,c3=st.columns([4,1,4])
       
with c1:
    st.warning("بعد از پرداخت لینک سورس کد برای شما باز میشود و بعد روی دکمه")
with c2:
    st.success(" ▷ Run ")
with c3:
    st.warning("کلیک میکنید و نتیجه پروژه رو اونجا میبینید و سورس کد بازی یا هر محصولی که خریداری کردید آماده تحویل شما داده میشه")

    
    
st.error("توجه : چه با سیستم کامپیوتر باشید چه با گوشی خیلی راحت میتونید کدها رو تغییر بدی و بازی یا هر محصولی که خریداری کردید رو میتونید به اسم خودتان ثبت کنید")


