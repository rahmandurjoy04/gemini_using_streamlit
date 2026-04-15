import streamlit as st
from api_calling import note_generator,quiz_generator
from working_with_audio import audio_transcription
from PIL import Image


st.title('Note Summary and Quiz Generator',anchor = False)
st.markdown('Upload maximum 3 Images to generate...')
st.divider()

with st.sidebar:
    st.header('Controls')
    #Image Upload
    images = st.file_uploader(
        "Upload your photo to analyze...",
        type = ['jpeg','png','jpg'],
        accept_multiple_files = True
        )
    st.subheader('Uploader Images')
    #Showing Images
    if images:
        if len(images)>3:
            st.error('Max 3 files allowed.')
        else:
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
    #Sending PIL_Images
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    #Setting Difficulty
    selected_option = st.selectbox(
        'Enter Difficulty of your Quiz',
        ('Easy','Medium','Hard'),
        index = None,
        placeholder = 'Select an Option'
    )
    if selected_option:
        st.markdown(f"You Selected **{selected_option}** difficulty.")
    
    pressed = st.button("Click the button to initiate",type = 'primary')


if pressed:
    if not images:
        st.error('You Must Upload Atleast one Image')
    if not selected_option:
        st.error('You Must Select a difficulty')
    if images and selected_option:
        #Note
        with st.container(border=True):
            st.subheader('Your Note')
            with st.spinner('AI is writing the notes from your images...'):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)
        #Audio Transcript
        with st.container(border=True):
            st.subheader('Audio Transcription')
            with st.spinner('AI is converting Audio from texts...'):
                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("'","")
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)
        #Quiz Generation
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")
            with st.spinner('AI is preparing Quizes for your images...'):
                generated_quizes = quiz_generator(pil_images,selected_option)
                st.markdown(generated_quizes)