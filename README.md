# Customer Support Message Extraction using LLM

This project demonstrates how an LLM can extract structured information from a customer support message.

The system extracts:

* **Intent**
* **Urgency**
* **Order Number**

The extracted information is returned as a valid JSON object.

## Example Input

```text
My order #12344 arrived damaged, and I need a refund immediately!
```

## Example Output

```json
{
    "intent": "Refund Request",
    "urgency": "High",
    "order_number": "12344"
}
```

## Technologies Used

* Python
* Google Gemini API
* JSON
* Google GenAI SDK

## Project Structure

```text
customer-support-llm-assessment/
│
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-support-llm-assessment.git
```

```bash
cd customer-support-llm-assessment
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set the Gemini API key

Create a Gemini API key and store it as an environment variable.

Windows Command Prompt:

```bash
set GEMINI_API_KEY=YOUR_API_KEY
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Linux/macOS:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

### 5. Run the program

```bash
python main.py
```

## Error Handling

The program includes basic error handling for:

* Missing API key
* API initialization errors
* API request failures
* Invalid JSON responses
* Missing required fields
* Invalid urgency values

## Security

The API key is read from an environment variable and is not hard-coded in the source code.

Do not commit API keys or other credentials to GitHub.

## Assessment Objective

The purpose of this project is to demonstrate basic proficiency in:

* Python programming
* LLM API integration
* Structured information extraction
* JSON parsing
* Input/output validation
* Basic exception handling

```
```
