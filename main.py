```python
import os
import json
import sys

from google import genai
from google.genai import types


# --------------------------------------------------
# Configuration
# --------------------------------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print(
        "Error: GEMINI_API_KEY environment variable is not set.\n"
        "Please set your API key before running the program."
    )
    sys.exit(1)


# --------------------------------------------------
# Sample customer support message
# --------------------------------------------------

customer_message = (
    "My order #12344 arrived damaged, and I need a refund immediately!"
)


# --------------------------------------------------
# Initialize Gemini client
# --------------------------------------------------

try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    sys.exit(1)


# --------------------------------------------------
# LLM Extraction
# --------------------------------------------------

prompt = f"""
You are a customer support message classification system.

Extract the following information from the customer message:

1. intent:
   Identify the customer's main request.
   Example: "Refund Request"

2. urgency:
   Must be exactly one of:
   - "High"
   - "Medium"
   - "Low"

3. order_number:
   Extract the order number as a string.
   If no order number is present, return null.

Return ONLY the requested JSON object.

Customer message:
{customer_message}
"""


try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        ),
    )

except Exception as e:
    print(f"Error while calling Gemini API: {e}")
    sys.exit(1)


# --------------------------------------------------
# Parse and validate response
# --------------------------------------------------

try:
    result = json.loads(response.text)

except (json.JSONDecodeError, TypeError) as e:
    print(f"Error parsing LLM response as JSON: {e}")
    print("Raw response:")
    print(response.text)
    sys.exit(1)


# Required fields
required_fields = ["intent", "urgency", "order_number"]

missing_fields = [
    field for field in required_fields
    if field not in result
]

if missing_fields:
    print(
        "Error: Missing required fields: "
        + ", ".join(missing_fields)
    )
    sys.exit(1)


# Validate urgency
allowed_urgency = {"High", "Medium", "Low"}

if result["urgency"] not in allowed_urgency:
    print(
        f"Error: Invalid urgency value: {result['urgency']}"
    )
    sys.exit(1)


# --------------------------------------------------
# Print final JSON
# --------------------------------------------------

print("\nExtracted Customer Support Information:")
print(json.dumps(result, indent=4))
```
