import streamlit as st
import requests




with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


merchant_id = "9a4ba04b-36e8-4bde-b074-d4a34f05cb2f"


col1,col4,col3 = st.columns(3)


            

with col1:
    with st.expander("هنر راهپیمایی", expanded=True):
        st.image("img/app1.png")
        col1,col2=st.columns([5,1])
        with col1:    
            st.caption("یک برنامه هنری پیکسلی با پیچ و تاب: پیکسل ها دایره هستند و با استفاده از الگوریتم مربع های راهپیمایی به پیکسل های دیگر در کنار خود متصل می شوند.")
        with col2:
            st.image("img/js.png",width=20)
        
        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)

        st.markdown("[دانلود رایگان](https://replit.com/@Samalander/Marching-Art?v=1#index.html)")
           





with col4:
    with st.expander("تولید رنگ ها", expanded=True):
        st.image("img/color.png")
        col1,col2=st.columns([5,1])
        with col1:    
            st.caption("رنگ های گرادیان تولید می کند و می توانید آن کد را کپی کند.")
        with col2:
            st.image("img/js.png",width=20)
            st.image("img/html.png",width=20)
            st.image("img/css.png",width=20)
        
        
        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)

        st.markdown("[دانلود رایگان](https://replit.com/@Kundanaks/GenerateGradientColors?v=1#script.js)")
            
    #  DIGI QESHM



with col3:
    with st.expander("✨ فوتو قشمی", expanded=True):
        st.image("img/photo.png")
        col1,col2=st.columns([5,1])
        with col1:    
            st.caption("برنامه ویرایش عکس که میتونید فایل مورد نظر رو آپلود کنید و عرض و ارتفاع آن را مشخص کنید و فایل ویرایش شده رو دانلود کنید")
        with col2:
            st.image("img/p.png",width=20)
        
        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)

        if st.markdown("1000 تومان"):
            url = "https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
            data = {
                    "MerchantID": merchant_id,
                    "Amount": 1000,
                    "Description": "فروشگاه عبدالله",
                    # 'Mobile': mobile,
                    # 'Email': email,
                    # https://mega.nz/file/lqcFWJiS#95xhq3HLE0ihOiJcxT5IvXmh8zkC00yOQFgCzuNWWVc
                    "CallbackURL": "https://replit.com/@AbdollahChelasi/photo#main.py",
                }

            response = requests.post(
                url,
                json=data,
                )
            if response.status_code == 200:
                result = response.json()
                if result["Status"] == 100:
                    payment_url = f'https://www.zarinpal.com/pg/StartPay/{result["Authority"]}'
                    st.markdown(f"[پرداخت و دانلود]({payment_url})")
                else:
                    st.error(f'Error: {result["Status"]}')
            else:
                st.error("Error: Could not create payment request.")
                
    

