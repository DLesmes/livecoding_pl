import base64
import os
import requests
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from app.settings import get_settings # Assuming settings.py is in the same 'app' directory

# Initialize settings and LLM
# This should be done once if the function is called multiple times,
# but for a single script, initializing here is fine.
settings = get_settings()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", # Using the recommended model alias from docs for latest flash
    google_api_key=settings.google_api_key 
)

def transcribe_video_from_url(video_url: str, output_txt_file: str) -> bool:
    """
    Downloads a video from a URL, sends it to Google Gemini for transcription,
    and saves the transcript to a text file.

    Args:
        video_url: The URL of the video to transcribe.
        output_txt_file: The path to save the transcript.

    Returns:
        True if successful, False otherwise.
    """
    if not settings.google_api_key:
        print("Error: GOOGLE_API_KEY not found in .env file or environment variables.")
        print("Please ensure your GOOGLE_API_KEY is set in the .env file in the project root.")
        return False

    print(f"Downloading video from {video_url}...")
    try:
        response = requests.get(video_url, stream=True, timeout=60) # Added timeout
        response.raise_for_status()  # Raise an exception for bad status codes

        # It's safer to save to a temporary file then read,
        # especially for larger videos, to avoid holding everything in memory.
        temp_video_path = "temp_video.mp4"
        with open(temp_video_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Video downloaded successfully.")

        print("Reading and encoding video...")
        with open(temp_video_path, "rb") as video_file:
            encoded_video = base64.b64encode(video_file.read()).decode("utf-8")
        
        # Clean up the temporary video file
        os.remove(temp_video_path)
        print("Video encoded.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading video: {e}")
        return False
    except IOError as e:
        print(f"Error processing video file: {e}")
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path) # Clean up if download succeeded but file ops failed
        return False

    print("Sending video to Gemini for transcription...")
    try:
        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    # Prompt asking for transcription
                    "text": "Transcribe this video. Provide only the spoken words as text.",
                },
                {
                    "type": "media", # Corrected type based on documentation for video/audio
                    "data": encoded_video,
                    "mime_type": "video/mp4", # Assuming mp4, adjust if needed
                },
            ]
        )
        
        # Invoke the model
        # Note: "gemini-2.5-pro-flash" might be a user-friendly name.
        # The actual model name might be like "gemini-1.5-flash-latest" or similar.
        # For gemini-1.5-flash-latest, it has good multimodal capabilities.
        ai_response = llm.invoke([message])
        transcript = ai_response.content

        print("Transcription received.")

        # Save the transcript to a file
        with open(output_txt_file, "w", encoding="utf-8") as f:
            f.write(transcript)
        print(f"Transcript saved to {output_txt_file}")
        return True

    except Exception as e:
        print(f"Error during transcription or saving: {e}")
        return False

if __name__ == '__main__':
   
    video_url_to_transcribe = "http://mdstrm.com/video/66973751147b59f38e6c08f9.mp4"
    output_file = "video_transcript.txt"
    
    success = transcribe_video_from_url(video_url_to_transcribe, output_file)
    if success:
        print("Transcription process completed successfully.")
    else:
        print("Transcription process failed.")
