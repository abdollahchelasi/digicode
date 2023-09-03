import streamlit as st

from st_pages import Page, show_pages, add_page_title



st.set_page_config(page_title="فروشگاه دیجی کد", layout="wide",page_icon="img/digicode.png")



with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)




st.image("img/digicode.png",width=200)

st.divider()
# https://9n2mf8-38083.csb.app/cljhg910a000ifqqj6a3k1eq9

# Optional -- adds the title and icon to the current page
# add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    
    [
        
        Page("app.py", "صفحه اصلی", "🏠"),
        Page("page/game.py", "ساخت بازی", ":books:"),
        Page("page/application.py", "ساخت برنامه", ":books:"),
        Page("page/arz.py", "ارز دیجیتال", ":books:"),
        Page("page/rahnama.py", "راهنما", ":books:"),
    ]
    
)


    
st.success("""
فروشگاه آموزشی دیجی کد با کلی سورس های آماده و اینکه بتونم با  کدهای کمتری یک برنامه کامل بسازم و اینکه سعی میکنم کسانی که برنامه نویسی بلد نیستن و علاقه دارن همچین پروژه هایی  بسازن و نمیخوان خیلی درگیر برنامه نویسی باشن پروژه هایی که با علامت ✨ روی پروژه ها برچسب زده شده رو اینجور پروژه ها برنامه های کامل زده شده و کد کمتری دارن 

        """
    
   
)










st.divider()

st.caption("""
           برای سفارش محصولات آموزشی که میخوای داخل دیجی کد قرار بگیره و مشکلات دیگری که دارید رو داخل فرم پایین , موضوعات و شماره تماس تون رو اضاف کنید در اسرع وقت پیگیری خواهد شد
           """)

contact_form="""
        <form action="https://formsubmit.co/abdollah.chelasi@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="نام شما" required>
        <input type="email" name="email" placeholder="شماره تماس" required>
        <textarea name="message" placeholder="موضوعات"  required ></textarea>
        <br/>
        <button type="submit" class="b">ارسال</button>
        </form> 
        """

left , right = st.columns(2)

with left:
    st.markdown(contact_form,unsafe_allow_html=True)

with right:
    st.markdown("[💬 ارسال پیام](sms:00989335825325)")
    st.markdown("[📞 تماس](tel:00989335825325)")
    
st.divider()
st.markdown("[طراح و برنامه نویس : عبداالله چلاسی](https://abdollahchelasi.ir)")
