import streamlit as st
import time

from config import APP_TITLE, APP_DESCRIPTION, STYLES
from captioner import ImageCaptioner
from image_processor import process_uploaded_image, resize_image_for_display

st.set_page_config(page_title=APP_TITLE, layout="wide", page_icon="🖼️")

@st.cache_resource
def load_captioner():
    with st.spinner("Loading AI models (this may take a minute on first run)..."):
        return ImageCaptioner()

def main():
    st.title(APP_TITLE)
    st.markdown(APP_DESCRIPTION)
    
    captioner = load_captioner()
    
    # Sidebar
    st.sidebar.header("Configuration")
    selected_style = st.sidebar.selectbox("Caption Style", options=list(STYLES.keys()))
    st.sidebar.info(STYLES[selected_style])
    
    # Main area
    st.subheader("Upload Images")
    uploaded_files = st.file_uploader(
        "Choose images (JPG, PNG, JPEG)", 
        type=["jpg", "jpeg", "png"], 
        accept_multiple_files=True
    )
    
    if uploaded_files:
        st.write(f"**{len(uploaded_files)} image(s) loaded.**")
        
        if st.button("Generate Captions", type="primary"):
            progress_bar = st.progress(0)
            cols = st.columns(min(3, len(uploaded_files)))
            
            for i, uploaded_file in enumerate(uploaded_files):
                image = process_uploaded_image(uploaded_file)
                display_image = resize_image_for_display(image)
                
                start_time = time.time()
                caption = captioner.generate_caption(image, style=selected_style)
                latency = time.time() - start_time
                
                col_idx = i % 3
                with cols[col_idx]:
                    st.image(display_image, use_column_width=True)
                    st.success(caption)
                    st.caption(f"⏱️ Latency: {latency:.2f}s | Style: {selected_style}")
                
                progress_bar.progress((i + 1) / len(uploaded_files))
            
            st.balloons()

if __name__ == "__main__":
    main()
