import streamlit as st
import time
# import streamlit as st

st.header('Welcome to our Prediction Model', divider='rainbow')
st.header(':blue[_FutureForge_] :green[is] :red[Advanced and Unique] :crown:')




st.info('You Can Find Here!!')




st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages\Company_details.py", label="Company Details", icon="📜")
# st.success('This is a success message!', icon="✅")
st.page_link("pages\About_us.py", label="About Us", icon="ℹ️")
st.page_link("pages\Predction.py", label="Prediction", icon="📌")
# st.page_link("app.py", label="Prediction", icon="4️⃣")
st.page_link("https://naukri-dev.netlify.app/#", icon="👉",label="Aim🔎Seeker")


def main():
    st.info('Registration', icon="ℹ️")
    
    # Text input for name
    name = st.text_input("Name")
    
    # Text input for email
    email = st.text_input("Email")
    
    # Text input for phone number
    phone_number = st.text_input("Phone Number")
    
    agree = st.checkbox('I agree')
    if agree:
        st.write('Great!')
    
    # Submit button
    if st.button("Submit"):
        with st.spinner('Wait for it...'):
            time.sleep(5)
        # st.success('Done!')

        if name and email and phone_number:
            st.toast("Welcome to our DataSciHub!")
        else:
            st.error("Please fill out all the fields.")

if __name__ == "__main__":
    main()


# st.caption('This is a string that explains something above.')
# st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')



# image

# import streamlit as st
# from PIL import Image
# import numpy as np

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer as a PIL Image:
#     img = Image.open(img_file_buffer)

#     # To convert PIL Image to numpy array:
#     img_array = np.array(img)

#     # Check the type of img_array:
#     # Should output: <class 'numpy.ndarray'>
#     st.write(type(img_array))

#     # Check the shape of img_array:
#     # Should output shape: (height, width, channels)
#     st.write(img_array.shape)




# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# import streamlit as st
# import numpy as np

# tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
# data = np.random.randn(10, 1)

# tab1.subheader("A tab with a chart")
# tab1.line_chart(data)

# tab2.subheader("A tab with the data")
# tab2.write(data)




