import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

PROMPT_TEMPLATE = """
You are a compliance auditor AI. Analyze the following log entries for suspicious or risky activity.

Log entries:
{entries}

Rules:
- Flag 3+ failed logins from the same IP.
- Flag failed logins to sensitive accounts (admin/root).
- Note unusual hours or actions.

Return:
- Summary of findings
- Risk level (Low, Medium, High)
- Recommended actions
"""

def analyze_with_llm(entries):
    try:
        formatted_logs = "\n".join([str(e) for e in entries])
        prompt = PROMPT_TEMPLATE.format(entries=formatted_logs)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cybersecurity compliance assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.2
        )

        return response.choices[0].message['content']
    except Exception as e:
        print(f"[ERROR] LLM analysis failed: {e}")
        return "Risk analysis failed due to LLM error."
