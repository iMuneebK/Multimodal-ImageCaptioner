# 🖼️ AI Image Captioning System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red)
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B)

An end-to-end AI application that generates intelligent, context-aware captions for images using state-of-the-art Vision-Language models.

## ✨ Features
- **Advanced Vision-Language Modeling:** Utilizes Salesforce's `BLIP-image-captioning-base` for accurate scene understanding.
- **Style Refinement:** Generate captions in different styles (Descriptive, Creative, Technical).
- **Batch Processing:** Upload and process multiple images concurrently.
- **Interactive UI:** Clean, responsive web interface built with Streamlit.

## 🏗️ Architecture
```mermaid
graph LR
    A[User] -->|Uploads Image| B(Streamlit UI)
    B --> C{Image Processor}
    C --> D[BLIP/ViT-GPT2 Model]
    D --> E(Text Decoder)
    E -->|Returns Caption| B
```

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-image-captioning.git
   cd ai-image-captioning
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📊 Results / Demo
*(Include screenshots of your running application here)*
- Upload interface with multiple images
- Captions generated with different style modifiers

## 🛠️ Tech Stack
- **Framework:** PyTorch
- **Models:** Hugging Face Transformers
- **Frontend:** Streamlit
- **Image Processing:** Pillow (PIL)
