import streamlit as st

st.title("Tacker and Cheddar little website")
st.subheader("Αμαν βρε Ταααααακ")
st.write("This site is for tucker and Cheddar!!"
         "Do you want to know more!???")

yes_button = st.button("Yes", key="yes")
no_button = st.button("No", key="no")

if yes_button:

    with st.expander("Samen at Giannena"):
        st.image(image="IMG_0633.jpeg")
        video_url = "https://www.youtube.com/watch?v=Lc6db8qfZEw"
        st.video(video_url)

    with st.expander("Samen in het treintje"):
        st.image(image="IMG_1240.jpeg")
        video_url_1 = "https://www.youtube.com/watch?v=LGrpsZ7BsQA"
        st.video(video_url_1)

elif no_button:
    st.text("Ειναι σωστο τωρα αυτοοοο!?")
    st.image(image="lp_image.jpeg")

st.text("IL still loading. Yes yes yes. 100 for a cup.")
