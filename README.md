# Simplechatbot

[![Python Version](https://img.shields.io/badge/python-^3.12-blue.svg)](https://www.python.org/downloads/)
[![Gradio Version](https://img.shields.io/badge/gradio-^5.0.1-green.svg)](https://gradio.app/)
[![Poetry Version](https://img.shields.io/badge/poetry-1.8.3-orange.svg)](https://python-poetry.org/)

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This chatbot leverages large language models (LLMs) from multiple providers (OpenAI, Anthropic, Google), allowing users to switch between different models seamlessly.

## Installation

### Prerequisites

- **Python**: Version ^3.12
- **Poetry**: Version 1.8.3

### Clone the Repository

```bash
git clone https://github.com/mbyta/simplechatbot.git
cd simplechatbot
```

### Install Dependencies
```bash
poetry install
```

### Set environment variables
Create a `.env` file from `.env.example` and set the key values

## Usage
Start the application by running the following command:
```bash
poetry run python src/simplechatbot/main.py
```
