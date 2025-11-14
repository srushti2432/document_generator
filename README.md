# AI Document Generator

An AI-powered technical documentation generator built using Google Gemini.

## Document Types

* **BRD** – Business Requirements Document

* **HLD** – High-Level Design

* **LLD** – Low-Level Design

* **FSD** – Functional Specification

* **Mapping Sheet** – Functional ↔ Solution Mapping

* **PPT** –  Overview Presentation

This tool streamlines documentation creation and ensures consistency across all deliverables.

## Key Features
* BRD Generated Only from Requirements

* The BRD is created exclusively from user requirements.

* It never uses or references uploaded code.

* Captures business goals, scope, problem statement, and expected outcomes.

 # Code Upload (ZIP-Based Python Parsing)

* Users may upload a ZIP of their Python project to enhance technical documents.

* When a ZIP is uploaded, the system:

    * Extracts all .py files

    * Reads entire source code

    * Builds an AST for structured analysis

    * Extracts:

         * function names

         * arguments

         * return types

         * docstrings

         * 1000-character code preview

Provides full file text (up to 2000 chars each)

Produces a structured Function Index


 ## Installation 
### Step A: Install dependencies
``` pip install -r requirements.txt ```

### Step B: Add your Gemini API key
``` GEMINI_API_KEY=your_api_key_here ```

``` python chatbot_main.py ```

 ## Usage Guide 
### Step 1: Provide Requirements

* Enter your project requirements in plain text.
* BRD is generated only from requirements — no code is used.

### Step 2: Upload Code 

* Upload a .zip file of your Python code.
* Used for HLD, LLD, FSD, Mapping Sheet, PPT.
* BRD does not use the ZIP code.

### Step 3: Choose Documents to Generate

* Select one document:

  * BRD

  * HLD

  * LLD

  * FSD

  * Mapping Sheet

  * PowerPoint

### Step 4: Download Final Documents

* Receive fully formatted, ready-to-use files:

  * DOCX → BRD, HLD, LLD, FSD

  * XLSX → Mapping

  * PPTX → Presentation
