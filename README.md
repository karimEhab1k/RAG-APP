# P-RAG

P-RAG APP is a personal Retrieval-Augmented Generation (RAG) app. You upload your personal documents, ask any question in plain language, and the app searches your files for the most relevant passages and uses them to generate an accurate answer.

Ask questions about your own documents and get answers grounded in what you uploaded.

## Requirements
-Python 3.9 or higher.

-An API key for your LLM provider (if applicable)

### Install Python using Miniconda
1) Download and install Miniconda from official documentation: https://docs.conda.io/en/latest/
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```

3) Activate the environment:
```bash
$ conda activate mini-rag
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.