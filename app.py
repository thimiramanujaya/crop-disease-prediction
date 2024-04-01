import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow_hub as hub
from streamlit_option_menu import option_menu
import crop_info
import test_images


st.title('Crop Disease Prediction')


def main():

  selected_menu = option_menu(
      menu_title=None,
      options=["Rice", "Potato", "Tomato", "Bellpepper", "Cinnamon"],
      orientation="horizontal",
  )


  def load_content(crop):
      file_uploaded = st.file_uploader(f'Choose an image of a {crop} leaf...', type='jpg')
      if file_uploaded is not None:
          image = Image.open(file_uploaded)
          st.write("Uploaded Image.")
          resized_image = image.resize([350, 350])
          st.image(resized_image)
          final_pred, confidence, consequences, remedies = predict_class(image, crop)
          st.write(f'<span style="font-size:20px; color:#808080">Prediction : {final_pred}</span>', unsafe_allow_html=True)
          st.write(f'<span style="font-size:20px; color:#808080">Confidence : {confidence}%</span>', unsafe_allow_html=True)
          st.write('<span style="font-size:20px; color:#808080">Consequences : {}</span>'.format(', '.join(consequences)), unsafe_allow_html=True)
          st.write('<span style="font-size:20px; color:#808080">Remedies : {}</span>'.format(', '.join(remedies)), unsafe_allow_html=True)

      st.write('<span style="font-size:24px;"> Test a sample image below, by simply drag and drop</span>', unsafe_allow_html=True)
    
      def display_images(x):
          for col in cols:
            with col:
               st.image(test_images.images_info[crop][x]['path'])
               st.write(f'''<div style="width:100%; text-align:center;"> <span> {test_images.images_info[crop][x]['name']} </span> </div>''', unsafe_allow_html=True)
               x = x+1
          
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

      elif crop=='cinnamon':
          col1, col2, col3 = st.columns(3)
          cols = [col1, col2, col3]
          display_images(0)
          


  if selected_menu == "Rice":
      load_content("rice")

  elif selected_menu == "Potato":
      load_content("potato")

  elif selected_menu == "Tomato":
      load_content("tomato")

  elif selected_menu == "Bellpepper":
      load_content("bellpepper")
    
  elif selected_menu == "Cinnamon":
      load_content("cinnamon")



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
    </style>
'''

st.markdown(blockcontainer, unsafe_allow_html=True)

