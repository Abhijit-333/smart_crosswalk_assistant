#   🚦 Smart Crosswalk Assistant

A **real-time computer vision system** designed to help pedestrians, especially the visually impaired and elderly to cross roads safely.  
The system detects **traffic signals**, **approaching vehicles**, and **crosswalk lines**, and provides **audio feedback** to guide safe crossing.

---

## 🚀 Features
- 🧠 **Real-time object detection** using YOLOv8 (traffic lights, vehicles, pedestrians)  
- 👁️ **Crosswalk segmentation** to detect lane boundaries  
- 🔊 **Audio guidance** (e.g., “Wait, red light”, “Safe to cross”)  
- ⚡ Built for real-world conditions: variable lighting, moving traffic, and occlusions  

---
## 💡 To do
   
    ☑︎ Real-time detection with YOLOv8 
    ☐ Add crosswalk line segmentation (DeepLab / Segment Anything)
    ☐ Integrate vehicle motion prediction
    ☐ Deploy on mobile (TensorFlow Lite / ONNX)
    ☐ Add GPS + vibration feedback for visually impaired users

## ⚙️ Setup (Conda)
 -bash terminal
#Clone the repository

    
    git clone https://github.com/Abhijit-333/smart_crosswalk_assistant.git
    cd smart_crosswalk_assistant

    #Create and activate environment
    
    conda env create -f environment.yml
    conda activate crosswalk

Run the demo for detection
-python src/detection.py
 


🧠 Tech Stack

    -Python 3.10
    -YOLOv8 (Ultralytics)
    -PyTorch
    -OpenCV
    -Matplotlib
    -pyttsx3 (Text-to-Speech)

🧾 License

This project is licensed under the MIT License

“Empowering safety through intelligent vision.”
