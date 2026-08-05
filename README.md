# 📊 Mini AI-Powered EDA Report Generator

An interactive Streamlit-based Exploratory Data Analysis (EDA) application that helps users analyze CSV datasets with visualizations and generate Pandas code using Google's Gemini AI.

---

## 🚀 Features

- 📂 Upload CSV datasets
- 👀 View complete dataset
- 📋 Dataset overview
  - Number of rows
  - Number of columns
  - Duplicate records
  - Data types
- 🔍 Missing value analysis
- 📈 Summary statistics
- 🔗 Correlation analysis
- 📊 Distribution plots for numerical columns
- 🤖 AI Pandas Assistant using Gemini API
  - Generates executable Pandas code based on natural language queries

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Google Gemini API (google-genai)

---

## 📁 Project Structure

```
Mini-EDA/
│── app.py
│── requirements.txt
│── README.md
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/ZoyaFarheen2603/mini-eda-AI-Powered.git
```

Go to the project folder:

```bash
cd mini-eda-AI-Powered
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔑 Gemini API Key

The AI Pandas Assistant requires a free Gemini API Key.

Steps:

1. Visit:
   https://aistudio.google.com/app/apikey

2. Create a free Gemini API Key.

3. Open the application.

4. Navigate to **AI Pandas Assistant**.

5. Paste your API key when prompted.

> Your API key is never stored in the project.

---

## 🤖 AI Pandas Assistant

Ask questions in natural language such as:

- Show the first 10 rows
- Display summary statistics
- Count missing values
- Show average marks department-wise
- Find students with marks greater than 80
- Sort students by marks
- Group data by department

The assistant generates executable Pandas code based on your request.

---

## 📸 Application Features

- Dataset Preview
- Dataset Overview
- Missing Value Analysis
- Summary Statistics
- Correlation Heatmap
- Distribution Visualization
- AI-Powered Pandas Code Generation

---

## 📌 Future Enhancements

- Execute generated Pandas code automatically
- Download EDA report as PDF
- Interactive visualizations
- Additional chart types
- AI-generated insights and recommendations

---

## 👩‍💻 Author

**Zoya Farheen**

GitHub:
https://github.com/ZoyaFarheen2603

---