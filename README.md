# Paper2Experiment 🧪

## AI Research Replication Engine

**Problem**: Most AI papers cannot be reproduced.

**Solution**: Automated paper-to-experiment pipeline.

### What it does:

1. 📄 **Takes an arXiv paper PDF** - Upload or provide arXiv URL
2. 🧠 **Extracts methodology automatically** - Uses Gemma 4 to parse architecture, hyperparameters, datasets
3. 💻 **Generates runnable code skeleton** - PyTorch/TensorFlow boilerplate with model structure
4. ⚙️ **Creates experiment configs** - YAML/JSON configs with all hyperparameters
5. 📊 **Produces reproducibility score** - Rates paper completeness (0-100%)

### Why it matters:

Researchers spend **hundreds of hours** trying to reproduce papers. This tool automates the initial setup, letting you focus on validation and extension.

### Quick Start:

```bash
pip install -r requirements.txt
ollama pull gemma4:26b
streamlit run app.py
```

### Tech Stack:

- **Model**: Gemma 4 (26B) via Ollama - Local, private processing
- **PDF Parsing**: pypdf, pdfplumber
- **Code Generation**: Structured prompts for reproducible outputs
- **Frontend**: Streamlit

### License: MIT