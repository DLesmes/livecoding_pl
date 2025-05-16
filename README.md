# 🎬 VidScribe & SumIt AI Wizard 🧙‍♂️

Welcome to the VidScribe & SumIt AI Wizard! This friendly Python project uses FastAPI and the magic of Google Gemini models (via LangChain) to help you with video transcription and text summarization. Let's turn those long videos and texts into easy-to-digest information! 🎉

## 🌟 Overview

This project provides a simple yet powerful backend service built with FastAPI. It leverages cutting-edge AI to:
1.  **Transcribe Videos**: Give it a video URL, and it will fetch the audio and provide you with a text transcript.
2.  **Summarize Text**: Feed it a transcript (or any long text), and it will generate a concise summary.

Perfect for students, content creators, researchers, or anyone looking to quickly understand video content or lengthy documents!

## ✨ Features

*   **FastAPI Backend**: Robust and modern API framework.
*   **Google Gemini Integration**: Utilizes powerful multimodal (`gemini-1.5-flash-latest`) and text models via `langchain-google-genai`.
*   **Video Transcription**: Downloads video from a URL and generates a transcript. 📼➡️📄
*   **Text Summarization**: Creates concise summaries from provided text. 📜➡️📝
*   **Environment Configuration**: Easy setup with a `.env` file for your API keys.
*   **Modular Design**: Separate processors for video and chat/text tasks.
*   **`uv` for Environment Management**: Modern and fast virtual environment setup.

## 🛠️ Getting Started

Follow these steps to get the AI Wizard up and running on your local machine.

1.  **Clone the Repository (if you haven't already)**:
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name> 
    ```
    (Replace `<your-repository-url>` and `<your-repository-name>` accordingly)

2.  **Create and Activate Virtual Environment using `uv`**:
    ```bash
    uv venv
    source .venv/bin/activate  # On Linux/macOS
    # .venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**:
    Create a `.env` file in the project root directory by copying the example or creating a new one:
    ```bash
    cp .env.example .env # If you have an .env.example
    # or
    touch .env
    ```
    Open the `.env` file and add your Google API Key:
    ```
    GOOGLE_API_KEY=your_actual_google_api_key_here
    ```
    Replace `your_actual_google_api_key_here` with your real key from Google AI Studio.

5.  **Run the FastAPI Application**:
    ```bash
    python app/main.py 
    # Or using uvicorn for development with auto-reload:
    # uvicorn app.main:app --reload
    ```
    The application will typically be available at `http://localhost:8000`.

## 🏃‍♂️ How to Use the Processors

This project includes scripts to directly process videos and text.

### 1. Transcribing a Video

*   **What it does**: Downloads a video from a URL, transcribes it using Gemini, and saves the transcript to `video_transcript.txt`.
*   **How to run**:
    ```bash
    # Ensure your .env file is set up and dependencies are installed
    python app/video_processor.py
    ```
    (You can modify the `video_url_to_transcribe` and `output_file` variables directly in the `if __name__ == '__main__':` block of `app/video_processor.py` if needed for different videos.)

### 2. Summarizing a Transcript (or any text)

*   **What it does**: Reads the `video_transcript.txt` (or any specified text file), sends it to Gemini for summarization, and saves the summary to `video_summary.txt`.
*   **How to run**:
    ```bash
    # Ensure video_transcript.txt exists (or specify your input file)
    python app/chat_processor.py
    ```
    (You can modify `input_transcript_file` and `output_summary_file` in `app/chat_processor.py` for different files.)

## 🤝 How to Contribute

Contributions make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**! ❤️

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again! ⭐

1.  **Fork the Project** (Click the 'Fork' button in the top right of this page).
2.  **Create your Feature Branch**:
    ```bash
    git checkout -b feature/AmazingFeature
    ```
3.  **Commit your Changes**:
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
4.  **Push to the Branch**:
    ```bash
    git push origin feature/AmazingFeature
    ```
5.  **Open a Pull Request**: Go to your fork on GitHub and click the 'New pull request' button.

We're excited to see what you build! 😊

---

Happy Coding! ✨
