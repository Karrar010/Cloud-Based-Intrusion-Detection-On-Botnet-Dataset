# 🔐 Cloud-Based Intrusion Detection on Botnet Dataset  

This project implements a **cloud-based intrusion detection system** (IDS) using a **Random Forest** model trained on the **Bot-IoT dataset**. The system detects malicious network activity and categorizes different types of cyber attacks. It includes a **Flask API** for real-time predictions and a **Tkinter-based GUI** for monitoring network traffic.

---

## 🚀 Features  

✅ **Machine Learning-Based Intrusion Detection** – Uses a Random Forest classifier for multi-level attack detection.  
✅ **Hierarchical Prediction Architecture** – Predicts **attack type, category, and subcategory**.  
✅ **Flask API for Real-Time Predictions** – Accepts network features and returns classified attacks.  
✅ **Tkinter-Based GUI** – Simulates packet monitoring and intrusion alerts.  
✅ **Cross-Origin Resource Sharing (CORS)** – Enables smooth integration with front-end applications.  

---

## 🏗️ Project Structure  

├── 📄 backend.py # Flask API for intrusion detection 

├── 🖥️ f.py # Tkinter-based GUI for live packet monitoring
 
├── 📊 intrusion-detection-on-botnet-dataset.ipynb # Jupyter Notebook for training the Random Forest model 

├── 📜 random_forest_model.pkl # Trained Random Forest model 

├── 🔊 alert.wav # Alert sound for detected intrusions

## Dependencies
- **pip install flask pandas numpy scikit-learn flask-cors tkinter pygame**


