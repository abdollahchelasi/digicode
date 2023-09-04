import streamlit as st
import requests




with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


merchant_id = "9a4ba04b-36e8-4bde-b074-d4a34f05cb2f"


col1,col3,col4 = st.columns(3)


            

with col1:
    with st.expander("بازی flappyBird", expanded=True):
        st.image("img/flap.png")

        c1,c2=st.columns([7,1])
       
        with c1:
            st.caption("معروف ترین بازی هایی که تو گوشی میکنید بای flappyBird")

        with c2:
            st.image("img/js.png",width=20)
            st.image("img/html.png",width=20)
            st.image("img/css.png",width=20)

        
        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)

        st.markdown("[دانلود رایگان](https://replit.com/@AraJan14/Flappy-Block?v=1#script.js)")
           
    
with col3:
    with st.expander("بازی ticked", expanded=True):
        st.image("img/tik.png")

        c1,c2=st.columns([7,1])
       
        with c1:
            st.caption("یک بازی نبرد مبتنی بر زمان که در آن همه چیز فقط زمانی حرکت می کند که شما انجام دهید")

        with c2:
            st.image("img/ts.png",width=20)
            

        
        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)

        st.markdown("[دانلود رایگان](https://replit.com/@IroncladDev/TAIme-is-ticking?v=1#code/main.ts)")    
                
with col4:
    with st.expander("بازی نبرد هوایی آنلاین", expanded=True):
        st.image("img/g3.png")

        c1,c2=st.columns([7,1])
       
        with c1:
            st.caption("""با دیگر بازیکنان بجنگید و مقام اول را کسب کنید!

چگونه بازی کنیم:
گام صدا: [ W,S ]
رول: [ A,D ]
یاو: [ Q,E ]
سرعت دادن: [ I ]
از سرعت خود بکاهید: [ K ]
شلیک: [ J ]""")

        with c2:
            st.image("img/js.png",width=20)
            

        
        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)

        st.markdown("[دانلود رایگان](https://replit.com/@pman10/3D-Flight-Simulator?v=1#index.html)")




with col1:
    with st.expander("بازی موج سواران مترو", expanded=True):
        st.image("img/sub.png")

        c1,c2=st.columns([7,1])
       
        with c1:
            st.caption("""بازی معروف Subway Surfers که در گوشی های اندرویدی بازی میکردید این بار خودت این بازی رو به اسم خودت ثبتش کن میتونی به سورس کد این بازی دست پیدا کنید و خیلی راحت کد ها رو تغییر بدی
                       بعد از زدن run کمی صبر کنید تا بازی اجرا شود
                       """)
        with c2:
            st.image("img/js.png",width=20)
            

        
        # st.image(url="https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png",width=60)

        st.markdown("[دانلود رایگان](https://replit.com/@WyattTurner22/Subway-Surfers?v=1#index.html)")    
     
