# Next Word Prediction using LSTM-RNN

## Overview

This project implements an intelligent text prediction system using Long Short-Term Memory (LSTM) neural networks. The model analyzes input text and predicts the most likely next word, enabling practical applications in text generation, autocomplete systems, and writing assistance tools.

**Key Features:**
- Fast and accurate next-word predictions
- Real-time inference through an interactive web interface
- Pre-trained LSTM model for immediate use
- Easily extensible for custom datasets

## Tech Stack

- **Python 3.x** - Core programming language
- **TensorFlow / Keras** - Deep learning framework
- **Streamlit** - Interactive web application framework
- **NumPy/Pandas** - Data processing

## Project Structure

```
.
├── app.py                    # Streamlit web application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── models/
│   └── next_word_model.h5   # Pre-trained LSTM model
└── notebooks/
    └── training.ipynb       # Model training notebook (Jupyter/Colab)
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip package manager
- 2GB+ free disk space (for model and dependencies)

### Installation

1. **Clone or download this repository:**
   ```bash
   git clone <repository-url>
   cd Next-Word-Prediction-LSTM-RNN
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the pre-trained model:**
   Download from: [Google Drive](https://drive.google.com/file/d/1NIoH0qW9Yao2yd3F2OHTQZ2I_HuU-z2V/view?usp=sharing)
   
   Extract the model file to the `models/` directory.

### Usage

**Run the Streamlit application:**
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`. Simply enter your text and the model will predict the next word!

## Model Details

- **Architecture:** LSTM-based Recurrent Neural Network
- **Input:** Text sequences (variable length)
- **Output:** Probability distribution over vocabulary
- **Training Data:** Large corpus of English text
- **Vocabulary Size:** ~10,000 words

## Performance

- Inference Time: <100ms per prediction (CPU)
- Accuracy: ~75% on validation set
- Model Size: ~4MB

## 🔮 Future Enhancements

- [ ] Implement Bidirectional LSTM for improved context understanding
- [ ] Expand training dataset for better coverage
- [ ] Full sentence generation capability
- [ ] Multi-language support
- [ ] Fine-tuning options for custom datasets
- [ ] GPU acceleration support




