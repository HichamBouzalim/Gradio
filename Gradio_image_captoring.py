# --- Import libraries ---
import gradio as gr  # For creating the web interface
from transformers import BlipProcessor, BlipForConditionalGeneration  # For image captioning
from PIL import Image  # For image processing

# --- Load the BLIP model and processor ---
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# --- Function to generate captions ---
def generate_caption(image):
    """
    Takes a PIL Image and generates a caption using the BLIP model.
    """
    # Convert the image into tensors for the model
    inputs = processor(images=image, return_tensors="pt")
    
    # Generate the caption sequence
    outputs = model.generate(**inputs)
    
    # Decode the generated sequence into readable text
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    return caption

# --- Wrapper function for Gradio ---
def caption_image(image):
    """
    Takes a PIL Image as input and returns the generated caption.
    Errors are caught and returned as text.
    """
    try:
        caption = generate_caption(image)
        return caption
    except Exception as e:
        return f"An error occurred: {str(e)}"

# --- Create Gradio interface ---
iface = gr.Interface(
    fn=caption_image,                 # Function to call when an image is uploaded
    inputs=gr.Image(type="pil"),      # Input is a PIL Image
    outputs="text",                   # Output is text (the generated caption)
    title="Image Captioning with BLIP",   
    description="Upload an image to generate a caption."
)

# --- Launch Gradio app ---
# server_name="0.0.0.0" → listens on all network interfaces
# server_port=7860 → port for the app (can be changed if needed)
iface.launch(server_name="0.0.0.0", server_port=7860)