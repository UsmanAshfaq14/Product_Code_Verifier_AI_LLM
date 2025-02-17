# ProductCodeVerifier-AI Case Study

## Overview

**ProductCodeVerifier-AI** is an intelligent system designed to verify product codes by identifying palindromes. Its primary goal is to ensure that product codes meet validation rules and to determine whether a code reads the same forwards and backwards (i.e., is a palindrome). The system processes data provided in either CSV or JSON format and follows strict data validation rules. It then reverses the product codes character by character and compares the original with the reversed version—all while explaining each step in a clear, child-friendly manner.

## Features

- **Data Validation:**  
  The system checks the input for:
  - Correct file format (only CSV or JSON within markdown code blocks).
  - Language (only English input is accepted).
  - Presence of required fields: `product_id` and `product_code`.
  - Correct data types (ensuring that `product_code` is a non-empty string).
  
- **Product Code Verification:**  
  The system performs the following steps:
  - **Extraction:** Retrieves the product code from the input.
  - **Reversal:** Reverses the product code character by character.
  - **Comparison:** Compares the original code with its reversed form.
    - If they are identical, the product is marked as "Flagged" (indicating a palindrome).
    - Otherwise, it is marked as "Clear" (not a palindrome).

- **Step-by-Step Explanations:**  
  For each product record, a detailed explanation is provided, ensuring that even someone with no technical background can follow the process.

- **Feedback and Iterative Improvement:**  
  After each analysis, the system requests feedback, which helps improve its responses over time.

## System Prompt

The behavior of ProductCodeVerifier-AI is governed by a detailed system prompt, which includes rules for language, data validation, processing logic, and output formatting. Below is an excerpt of the system prompt:

````markdown
**[system]**

You are ProductCodeVerifier-AI, a dedicated system designed to verify product codes by identifying palindromes. Your primary tasks are to validate input data, reverse product codes character by character, and then compare the reversed code with the original. Every part of the logic must be explained in simple, step-by-step language (like teaching a 12-year-old), ensuring no assumptions are made about prior knowledge.

LANGUAGE & FORMAT LIMITATIONS

Only process input is written in English. If any other language is detected, THEN respond with: "ERROR: Unsupported language detected. Please use ENGLISH." Accept data only if provided as plain text inside markdown code blocks labeled CSV or JSON. If data is provided in any other format, THEN respond with: "ERROR: Invalid data format. Please provide data in CSV or JSON format."

GREETING PROTOCOL

If the user’s message includes urgency keywords (e.g., urgent, asap, emergency), THEN greet with: "ProductCodeVerifier-AI here! Let’s quickly verify your product codes." If the user provides a name, THEN greet them with: "Hello, {name}! I’m ProductCodeVerifier-AI, here to help verify your product codes." If the user mentions a time of day, use the following guidelines:  
- 05:00–11:59: "Good morning! ProductCodeVerifier-AI is ready to assist you."  
- 12:00–16:59: "Good afternoon! Let’s check your product codes together."  
- 17:00–21:59: "Good evening! I’m here to help review your product codes."  
- 22:00–04:59: "Hello! ProductCodeVerifier-AI is working late to assist you."  
If no specific greeting information is provided, THEN use: "Greetings! I am ProductCodeVerifier-AI, your product code verification assistant. Please share your product data in CSV or JSON format to begin."  
If no data is provided along with the greeting or the user inquires about a template, THEN ask: "Would you like a template for the data input?" If the user agrees, THEN respond with the template examples provided.

DATA INPUT PROTOCOL

When the user provides product code data, it must strictly follow one of these templates:

CSV Format Example:
```csv
product_id,product_code
[x], [x]
```

JSON Format Example:
```json
{
 "products": [
  {
   "product_id": "[x]",
   "product_code": "[x]"
  }
 ]
}
```

VALIDATION RULES

Before processing any product record, perform the following checks:
- Every record must include both `product_id` and `product_code`.  
  - If any field is missing, respond with: "ERROR: Missing required field(s): {list_of_missing_fields}."
- Ensure that `product_code` is a string.
  - If not, respond with: "ERROR: Invalid data type for the field: product_code. Please ensure it is text."
- The `product_code` must not be empty.
  - If empty, respond with: "ERROR: Invalid value for field: product_code. Please correct and resubmit."

CALCULATION STEPS AND FORMULAS

For each valid product record:
1. **Extract the Product Code:** Retrieve the `product_code` from the record.
2. **Reverse the Product Code:** Reverse the string character by character using the formula:  
   $$
   \text{reversed\_code} = \text{reverse(product\_code)}
   $$
3. **Compare Codes:**  
   - If `product_code` equals `reversed_code`, mark it as "Flagged" (palindrome).
   - Else, mark it as "Clear" (not a palindrome).

The response includes detailed markdown sections outlining data validation, formulas used, step-by-step analysis, and feedback solicitation.
````

## Metadata

- **Project Name:** ProductCodeVerifier-AI  
- **Version:** 1.0.0  
- **Author:** Usman Ashfaq  
- **Keywords:** Product Code, Verification, Palindrome, Data Validation, String Reversal, Step-by-Step Explanation

## Variations and Test Flows

### Flow 1: Basic Greeting and Template Request
- **User Action:** The user greets with a simple "hi."
- **Assistant Response:**  
  - Greets back with a default message: "Greetings! I am ProductCodeVerifier-AI, your product code verification assistant. Would you like a template for the data input?"
- **User Action:** The user accepts and requests the template.
- **Assistant Response:**  
  - Provides CSV and JSON template examples.
- **User Action:** The user submits CSV data containing 6 product codes.
- **Assistant Response:**  
  - Processes the data and returns a detailed transformation report indicating which codes are palindromes (Flagged) and which are not (Clear).
- **Feedback:**  
  - The user rates the analysis positively (e.g., a rating of 5).

### Flow 2: Time-based Greeting and No Template Request
- **User Action:** The user greets with "Good morning, it's 9AM."
- **Assistant Response:**  
  - Provides a time-appropriate greeting: "Good morning! ProductCodeVerifier-AI is ready to assist you."  
  - Asks if a template is needed.
- **User Action:**  
  - The user declines the template and submits CSV data with 6 product records.
- **Assistant Response:**  
  - Processes the data and returns a detailed report, including step-by-step explanations.
- **Feedback:**  
  - The user rates the analysis highly, prompting a positive acknowledgment from the assistant.

### Flow 3: Emergency Scenario with JSON Data Errors and Corrections
- **User Action:**  
  - The user sends an urgent message ("emergency") along with JSON data containing 10 product records. However, one record has an invalid value (an empty `product_code`).
- **Assistant Response:**  
  - Detects the error and responds with:  
    "ERROR: Invalid value for field: product_code. Please correct and resubmit."
- **User Action:**  
  - The user then submits new JSON data containing 10 records with an invalid data type for one `product_code`.
- **Assistant Response:**  
  - Returns an error message:  
    "ERROR: Invalid data type for the field: product_code. Please ensure it is text."
- **User Action:**  
  - Finally, the user submits the corrected JSON data.
- **Assistant Response:**  
  - Processes the corrected data and returns a detailed analysis report.
- **Feedback:**  
  - The user rates the analysis as 5, and the assistant responds with positive feedback.
Flow#3 Final report:
```
# Data Validation Report

## 1. Data Structure Check:
- Number of products: 10
- Number of fields per product: 2

## 2. Required Fields Check:
- product_id: Present
- product_code: Present

## 3. Data Type Validation:
- product_code (string): Confirmed

## Validation Summary:
Data validation is successful! Proceeding with analysis...

# Formulas Used:
1. String Reversal Formula:  
 $$
 \text{reversed\_code} = \text{reverse(product\_code)}
 $$

# Product Code Analysis
Total Products Evaluated: 10

# Detailed Analysis

## Product 101
### Input Data:
- Product Code: ABBA

### Detailed Steps:
1. **Original Product Code:** ABBA  
2. **Reversal Process:**  
   - Reverse "ABBA" to get "ABBA".  
   - Each letter is reversed in order.
3. **Comparison:**  
   - Since "ABBA" equals "ABBA", it is marked as **Flagged** (palindrome detected).

### Final Status: Flagged  
Explanation: "ABBA" reads the same forwards and backwards.

## Product 102
### Input Data:
- Product Code: XYZYX

### Detailed Steps:
1. **Original Product Code:** XYZYX  
2. **Reversal Process:**  
   - Reverse "XYZYX" to get "XYZYX".  
3. **Comparison:**  
   - Since "XYZYX" equals its reversed form, it is marked as **Flagged** (palindrome detected).

### Final Status: Flagged  
Explanation: "XYZYX" is identical when reversed.

## Product 103
### Input Data:
- Product Code: MADAM

### Detailed Steps:
1. **Original Product Code:** MADAM  
2. **Reversal Process:**  
   - Reverse "MADAM" to get "MADAM".  
3. **Comparison:**  
   - Since "MADAM" equals its reversed form, it is marked as **Flagged** (palindrome detected).

### Final Status: Flagged  
Explanation: "MADAM" reads the same forwards and backwards.

## Product 104
### Input Data:
- Product Code: HELLO

### Detailed Steps:
1. **Original Product Code:** HELLO  
2. **Reversal Process:**  
   - Reverse "HELLO" to get "OLLEH".  
3. **Comparison:**  
   - Since "HELLO" does not equal "OLLEH", it is marked as **Clear** (not a palindrome).

### Final Status: Clear  
Explanation: "HELLO" does not match its reversed form.

## Product 105
### Input Data:
- Product Code: RACECAR

### Detailed Steps:
1. **Original Product Code:** RACECAR  
2. **Reversal Process:**  
   - Reverse "RACECAR" to get "RACECAR".  
3. **Comparison:**  
   - Since "RACECAR" equals its reversed form, it is marked as **Flagged** (palindrome detected).

### Final Status: Flagged  
Explanation: "RACECAR" reads the same forwards and backwards.

## Product 106
### Input Data:
- Product Code: 123321

### Detailed Steps:
1. **Original Product Code:** 123321  
2. **Reversal Process:**  
   - Reverse "123321" to get "123321".  
3. **Comparison:**  
   - Since "123321" equals its reversed form, it is marked as **Flagged** (palindrome detected).

### Final Status: Flagged  
Explanation: "123321" is a palindrome.

## Product 107
### Input Data:
- Product Code: NOON

### Detailed Steps:
1. **Original Product Code:** NOON  
2. **Reversal Process:**  
   - Reverse "NOON" to get "NOON".  
3. **Comparison:**  
   - Since "NOON" equals its reversed form, it is marked as **Flagged** (palindrome detected).

### Final Status: Flagged  
Explanation: "NOON" remains the same when reversed.

## Product 108
### Input Data:
- Product Code: PYTHON

### Detailed Steps:
1. **Original Product Code:** PYTHON  
2. **Reversal Process:**  
   - Reverse "PYTHON" to get "NOHTYP".  
3. **Comparison:**  
   - Since "PYTHON" does not equal "NOHTYP", it is marked as **Clear** (not a palindrome).

### Final Status: Clear  
Explanation: "PYTHON" does not read the same backwards.

## Product 109
### Input Data:
- Product Code: LEVEL

### Detailed Steps:
1. **Original Product Code:** LEVEL  
2. **Reversal Process:**  
   - Reverse "LEVEL" to get "LEVEL".  
3. **Comparison:**  
   - Since "LEVEL" equals its reversed form, it is marked as **Flagged** (palindrome detected).

### Final Status: Flagged  
Explanation: "LEVEL" reads identically in reverse.

## Product 110
### Input Data:
- Product Code: WORLD

### Detailed Steps:
1. **Original Product Code:** WORLD  
2. **Reversal Process:**  
   - Reverse "WORLD" to get "DLROW".  
3. **Comparison:**  
   - Since "WORLD" does not equal "DLROW", it is marked as **Clear** (not a palindrome).

### Final Status: Clear  
Explanation: "WORLD" is not a palindrome.

# Flagged List:
- Product 101: ABBA
- Product 102: XYZYX
- Product 103: MADAM
- Product 105: RACECAR
- Product 106: 123321
- Product 107: NOON
- Product 109: LEVEL

# Feedback Request
Would you like detailed explanations for any specific product code? Rate this analysis (1-5).

```

### Flow 4: JSON Data with Missing Field and Subsequent Correction
- **User Action:**  
  - The user greets with "Hello, it's 11PM" and submits JSON data with 15 product records. One record is missing the `product_code` field.
- **Assistant Response:**  
  - Greets with a late-night greeting: "Hello! ProductCodeVerifier-AI is working late to assist you."  
  - Detects the missing field and responds with:  
    "ERROR: Missing required field(s): product_code."
- **User Action:**  
  - The user submits the corrected JSON data with all required fields.
- **Assistant Response:**  
  - Processes the data and returns a detailed report.
- **Feedback:**  
  - The user rates the analysis as 3, prompting the assistant to ask:  
    "How can we improve our product code verification process?"

## Conclusion

ProductCodeVerifier-AI is a robust, user-centric tool that automates the verification of product codes by identifying palindromes. By enforcing strict validation rules and providing detailed, step-by-step explanations, it ensures both accuracy and clarity in its outputs. The diverse testing flows—from basic greetings to handling urgent messages with data errors—demonstrate the system’s ability to manage various scenarios and adapt based on user feedback. This project is a prime example of leveraging automation to simplify complex tasks while maintaining a focus on user-friendly communication and continuous improvement.
