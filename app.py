import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow_hub as hub
from streamlit_option_menu import option_menu
import time
#from streamlit.components.v1 import html
import crop_info
import test_images


browseImage = None
sampleImage = None


st.title('Crop Disease Prediction')


def main():

  selected_menu = option_menu(
      menu_title=None,
      options=["Rice", "Potato", "Tomato", "Bellpepper", "Coconut"],
      orientation="horizontal",
  )

  def display_results(image, crop):
      st.write("Uploaded Image.")
      resized_image = image.resize([350, 350])
      col1, col2, col3 = st.columns(3)
      with col2:
       st.image(resized_image)
      final_pred, confidence, consequences, remedies = predict_class(image, crop)
      st.write(f'<span style="font-size:20px; color:#808080">Prediction : {final_pred}</span>', unsafe_allow_html=True)
      st.write(f'<span style="font-size:20px; color:#808080">Confidence : {confidence}%</span>', unsafe_allow_html=True)
      st.write('<span style="font-size:20px; color:#808080">Consequences : {}</span>'.format(', '.join(consequences)), unsafe_allow_html=True)
      st.write('<span style="font-size:20px; color:#808080">Remedies : {}</span>'.format(', '.join(remedies)), unsafe_allow_html=True)
      
      
  def load_content(crop):
      
      def display_images(x):
          for col in cols:
            with col:
               st.image(test_images.images_info[crop][x]['path'], caption=test_images.images_info[crop][x]['name'], use_column_width=True)
               #st.write(f'''<div style="width:100%; text-align:center;"> <span> {test_images.images_info[crop][x]['name']} </span> </div>''', unsafe_allow_html=True)
               
               if st.button("Upload", key=x):
                    global sampleImage
                    sampleImage = Image.open(test_images.images_info[crop][x]['path'])
                    st.toast('Scroll Down to View Results',icon='👇')
                    time.sleep(.5)
                    #img_file = open(test_images.images_info[crop][x]['path'], "rb")
               x = x+1
                   

      st.write('<span style="font-size:24px;">No image? Test a sample image below</span>', unsafe_allow_html=True)
        
      if crop=='rice':
          col1, col2, col3, col4 = st.columns(4)
          cols = [col1, col2, col3, col4]
          display_images(0)
      
      elif crop=='potato':
          col1, col2, col3 = st.columns(3)
          cols = [col1, col2, col3]
          display_images(0)
      
      elif crop=='tomato':
          col1, col2, col3, col4, col5 = st.columns(5)
          cols = [col1, col2, col3, col4, col5]
          display_images(0)
          display_images(5)
          
      elif crop=='bellpepper':
          col1, col2, col3 = st.columns(3)
          cols = [col1, col2, col3]
          display_images(0)

      elif crop=='coconut':
          col1, col2, col3, col4, col5 = st.columns(5)
          cols = [col1, col2, col3, col4, col5]
          display_images(0)
      

      file_uploaded = st.file_uploader(f'Choose an image of a {crop} leaf...', type=["jpg", "jpeg", "png"])
      if file_uploaded is not None:
          global browseImage
          browseImage = Image.open(file_uploaded)
    
      if sampleImage is not None:
          if browseImage is not None:
              st.warning('Please remove the current image, before test sample images', icon="⚠️")
              
              #st.warning('Do you want to remove the image, uploaded from your device?', icon="⚠️")
              #if st.button('Yes, Remove'):
              #    browseImage = None
              #    st.write('remved')
              #if st.button('No, Keep'):
              #    st.write('fine')

              #js = """alert('Need to remove')"""
              #html_code = f"<script>{js}</script>"
              #html(html_code)
              
          else:
            display_results(sampleImage, crop)
      

      if browseImage is not None:
        display_results(browseImage, crop)


  if selected_menu == "Rice":
      load_content("rice")

  elif selected_menu == "Potato":
      load_content("potato")

  elif selected_menu == "Tomato":
      load_content("tomato")

  elif selected_menu == "Bellpepper":
      load_content("bellpepper")
    
  elif selected_menu == "Coconut":
      load_content("coconut")


def predict_class(image, crop):
    with st.spinner('Loading Model...'):

        classifier_model = tf.keras.models.load_model(f'{crop}.h5')


    #shape = (256, 256, 3)
    model = tf.keras.Sequential([classifier_model])

    test_image = image.resize((crop_info.image_sizes[crop], crop_info.image_sizes[crop]))
    test_image = tf.keras.preprocessing.image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)

    class_name = crop_info.disease_info[crop]['class_name']

    prediction = model.predict(test_image)
    confidence = round(100 * (np.max(prediction[0])), 2)
    final_pred = class_name[np.argmax(prediction)]
    
    # Get remedies and consequences for the predicted disease
    consequences = crop_info.disease_info[crop][final_pred]['consequences']
    remedies = crop_info.disease_info[crop][final_pred]['remedies']
    
    
    return final_pred, confidence, consequences, remedies

if __name__ == '__main__':
    main()

blockcontainer = '''
    <style>
        div [data-testid="stAppViewBlockContainer"] {
            min-width: 65%;
        }

        div [data-testid="stHorizontalBlock"] div [data-testid="stButton"] {
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            bottom: 120px;
            opacity: 0;
        }

        div [data-testid="stHorizontalBlock"] div [data-testid="stButton"] button {
            box-shadow: rgba(0, 0, 0, .4) 0 3px 5px -1px,rgba(0, 0, 0, .34) 0 6px 10px 0,rgba(0, 0, 0, .22) 0 1px 18px 0;
            background-color: #ffffffcd;
            border: 2px solid #760be0;
            color: black;
        }

        div [data-testid="stHorizontalBlock"] div [data-testid="stButton"]:hover {
            opacity: 1;
        }

        div [data-testid="element-container"] iframe html body i.bi-caret-right {
            display: none;
            opacity: 0;
        }

        @media only screen and (max-width: 641px) {
            div [data-testid="stHorizontalBlock"] div [data-testid="stButton"] {
                position: relative;
                bottom: 10px;
                opacity: 1;
            }
            div [data-testid="stHorizontalBlock"] div [data-testid="stButton"] button {
                background-color: black;
                border-color: white;
                color: white;
            }
        }
    </style>
'''

st.markdown(blockcontainer, unsafe_allow_html=True)


