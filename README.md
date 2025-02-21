# 🏆 Flutter App Automation with Appium & Python

This repository contains an **Appium-based automation framework** for testing a Flutter mobile application using **Python**.

---

## 📌 Features
✅ Automates Flutter-based mobile apps  
✅ Uses `appium_flutter_finder` for element interactions  
✅ Supports **Android**  
✅ Works with **LambdaTest** cloud devices  
✅ Step-by-step setup instructions included  

---

## 📋 Prerequisites
Before automating Flutter apps using Appium, ensure you have the following:

### 🔹 **1. Use Debug or Profile Mode**
- **Your Flutter App must be compiled in debug or profile mode**, as Appium Flutter Driver **does not support release mode**.

### 🔹 **2. Add Dependencies to `pubspec.yaml`**
Add the following dependencies to your `pubspec.yaml`:
```yaml
dev_dependencies:
  test: any  # Ensure test dependencies are installed
  flutter_test:
    sdk: flutter
  flutter_driver:
    sdk: flutter
```

### 🔹 **3. Modify `main.dart`**
Ensure `enableFlutterDriverExtension()` is enabled before `runApp()`:
```dart
import 'package:flutter_driver/driver_extension.dart';

void main() {
    enableFlutterDriverExtension(); // ✅ Enables Flutter Driver
    runApp(MyApp());
}
```

### 🔹 **4. Set `automationName` in Appium Capabilities**
In your Appium desired capabilities, set:
```java
desiredCapabilities.setCapability("automationName", "flutter");
```

---

## 📤 Upload Your App to LambdaTest
Before running tests, you need to **upload your Flutter app (APK) to LambdaTest** and get the **app ID**.

### **1️⃣ Sign in to LambdaTest**
- Go to [LambdaTest](https://www.lambdatest.com/)
- Log in to your account

### **2️⃣ Upload Your App**
- Navigate to **App Automation** → **Upload App**
- Upload your `.apk` (Android) file
- Once uploaded, **copy the `app ID`** (e.g., `lt://APP1016045521739462030652329`)

### **3️⃣ Update `config.py` with App ID and Credentials**
Open `configs/config.py` and update:
```python
APPIUM_SERVER = "https://<USERNAME>:<ACCESS_KEY>@mobile-hub.lambdatest.com/wd/hub"

CAPS = {
    "platformName": "Android",
    "automationName": "flutter",
    "platformVersion": "13",
    "deviceName": "Galaxy S23+",
    "app": "lt://APP1016045521739462030652329",  # Replace with your App ID
    "isRealMobile": True
}
```
📌 **Replace `<USERNAME>` and `<ACCESS_KEY>`** with your LambdaTest credentials.  

---

## 🛠️ Step-by-Step Setup Instructions

### **1️⃣ Clone the Repository**
Open a terminal and run:
```bash
git clone https://github.com/belaletech/flutter_app_automation.git
cd flutter_app_automation
```

### **2️⃣ Create a Virtual Environment**
To keep dependencies isolated, create a virtual environment:
```bash
python -m venv venv
```
Activate the environment:  
- **Windows**:  
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:  
  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**
Install all required Python packages:
```bash
pip install -r requirements.txt
```

### **4️⃣ Start Appium Server**
Make sure you have **Appium installed**. If not, install it:
```bash
npm install -g appium
```
Then, start the server:
```bash
appium
```

### **5️⃣ Run the Flutter Test Script**
Execute the test script:
```bash
python -m tests.test_flutter_app
```

---

## 📁 Project Structure
```bash
flutter_app_automation/
│── configs/
│   ├── __init__.py
│   ├── config.py  # Stores Appium capabilities
│── tests/
│   ├── __init__.py
│   ├── test_flutter_calculator.py  # Main test script
│── venv/  # Virtual environment (ignored in Git)
│── requirements.txt  # Python dependencies
│── .gitignore  # Ignore unnecessary files
│── README.md  # Documentation
```

---

## 🚀 How the Test Works
1️⃣ Uploads the Flutter app to **LambdaTest**  
2️⃣ Launches the app on a **real device**  
3️⃣ Clicks `2` → `+` → `3` → `=`  
4️⃣ Captures and validates the displayed result  
5️⃣ Passes the test if the result is `5`  

---

## 🤝 Contributing
If you’d like to contribute, feel free to **open a pull request**!

## 📜 License
This project is **open-source** under the **MIT License**.
```

✅ What’s New in This Version?
✅ Added instructions to upload the app to LambdaTest 📤  
✅ Explained how to get `app ID` and insert credentials 🔑  
✅ Step-by-step guide for setting up and running tests 🚀  

