# Image Captioning with BLIP

This project enables automatic generation of descriptive captions for images using the **BLIP (Bootstrapped Language Image Pretraining)** model by Salesforce. A simple and interactive web interface is provided via **Gradio**, allowing users to upload an image and instantly receive a textual description.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Architecture](#architecture)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Error Handling](#error-handling)  
- [Notes](#notes)  
- [References](#references)  
- [License](#license)  

---

## Overview

The goal of this project is to provide a lightweight and accessible tool for image captioning that leverages state-of-the-art NLP and computer vision techniques. By combining the BLIP model with Gradio, this project allows:

- Fast, accurate image captioning.
- Easy testing and experimentation.
- Integration into larger projects or pipelines.

---

## Features

- **Automatic Image Captioning**: Generate meaningful captions for any uploaded image.
- **Interactive Web Interface**: Simple drag-and-drop image upload using Gradio.
- **LAN Accessibility**: Can be accessed from any device within the same local network.
- **Error Handling**: Graceful handling of invalid inputs or model errors.
- **Lightweight and Extensible**: Easy to integrate into other Python projects or web applications.

---

## Architecture

1. **BLIP Model**:  
   - `BlipProcessor` handles image preprocessing (resizing, normalization, tokenization).  
   - `BlipForConditionalGeneration` generates captions using the processed image tensors.  

2. **Gradio Interface**:  
   - Wraps the captioning function into a simple web interface.  
   - Accepts images as PIL objects and returns generated text.  

3. **Error Handling**:  
   - The app catches exceptions during caption generation and displays informative error messages.  

---

## Installation

1. **Clone this repository**:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
