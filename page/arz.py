import streamlit as st
import requests




with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


merchant_id = "9a4ba04b-36e8-4bde-b074-d4a34f05cb2f"


col1,col3 = st.columns(2)


            

with col1:
    with st.expander("✨ وبسایت ارز دیجیتال", expanded=True):
        st.image("img/arz.png")
        col1,col2=st.columns([5,1])
        with col1:    
            st.caption("نمایش آخرین چارت نماد های ارز دیجیتال")
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
                    "CallbackURL": "https://replit.com/@AbdollahChelasi/bitcoinPY#main.py",
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
                
    
with col3:
    with st.expander("✨ قیمت ارز دیجیتال", expanded=True):
        st.image("img/qarz.png")
        col1,col2=st.columns([5,1])
        with col1:    
            st.caption("نمایش آخرین قیمت ارز دیجیتال به دلار , قیمت رو به صورت لحظه ای مشاهده کنید")
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
                    "CallbackURL": "https://replit.com/@AbdollahChelasi/ARZ#main.py",
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
                
    
