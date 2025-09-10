# 🖼️ Build a Gradio Web App for BLIP Image Captioning

This project enables automatic generation of image captions using the **BLIP (Bootstrapped Language Image Pretraining)** model from Salesforce. An **interactive web interface** via **Gradio** allows users to upload images and instantly receive textual descriptions.

---

## 📑 Table of Contents

* [✨ Overview](#-overview)
* [⚡ Features](#-features)
* [🏗 Architecture](#-architecture)
* [💻 Installation](#-installation)
* [🚀 Usage](#-usage)
* [⚙️ Configuration](#-configuration)
* [🛠 Error Handling](#-error-handling)
* [📝 Notes](#-notes)
* [📚 References](#-references)
* [📄 License](#-license)

---

## ✨ Overview

This project provides a **lightweight, accessible tool** for image captioning that leverages modern NLP and computer vision techniques.

**Highlights:**

* Fast and accurate image captions
* Easy testing & experimentation
* Integration into larger projects or pipelines

---

## ⚡ Features

| Feature                          | Description                                                      |
| -------------------------------- | ---------------------------------------------------------------- |
| 🖼️ **Automatic Image Captions** | Generates meaningful captions for uploaded images                |
| 🌐 **Interactive Web Interface** | Drag-and-drop image upload using Gradio                          |
| 📡 **LAN Accessibility**         | Access from any device in the same network                       |
| ⚠️ **Error Handling**            | Invalid inputs or model errors are handled gracefully            |
| 🔧 **Lightweight & Extensible**  | Easy to integrate into other Python projects or web applications |

---

## 🏗 Architecture

1. **BLIP Model**

   * `BlipProcessor` → Image preprocessing (resize, normalization, tokenization)
   * `BlipForConditionalGeneration` → Generates captions from image tensors

2. **Gradio Interface**

   * Wraps the captioning function in a user-friendly web interface
   * Accepts PIL images and returns generated text

3. **Error Handling**

   * Catches exceptions and displays informative error messages

---

## 💻 Installation

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
python -m venv venv  # create virtual environment (optional)
# Activate:
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install torch transformers gradio pillow
```

> Requires Python 3.8 or higher

---

## 🚀 Usage

```bash
python app.py
```

* **Local (same machine)**: [http://127.0.0.1:7860](http://127.0.0.1:7860)
* **LAN (network devices)**:

  1. Find local IP (`ipconfig` / `ifconfig`)
  2. Open browser on another device: `http://YOUR_LOCAL_IP:7860`

---

## ⚙️ Configuration

* `server_name="0.0.0.0"` → allows access from all network interfaces
* `server_port=7860` → default, can be changed if needed

```python
iface.launch(server_name="0.0.0.0", server_port=7860)
```

---

## 🛠 Error Handling

* Invalid or corrupted image files are caught
* Exceptions during caption generation → displayed as errors in the web interface
* App does not crash due to unexpected inputs

---

## 📝 Notes

* **Internet Access**:

  * Configure port forwarding on the router
  * Optional: use a tunneling service like **ngrok**
* **Performance**:

  * GPU recommended for faster inference
  * CPU inference possible, slower for large images

---

## 📚 References

* [BLIP Model on Hugging Face](https://huggingface.co/salesforce/blip)
* [Gradio Documentation](https://gradio.app/docs/)
* [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
