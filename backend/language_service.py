import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

client = TextAnalyticsClient(
    endpoint=os.getenv("AZURE_LANGUAGE_ENDPOINT"),
    credential=AzureKeyCredential(os.getenv("AZURE_LANGUAGE_KEY"))
)

def generate_parent_insight(logs):
    if not logs:
        return "No routine data yet."

    # Find steps that took longer than average
    times = [log["time_taken"] for log in logs]
    avg_time = sum(times) / len(times)

    slower_steps = [
        log["step"]
        for log in logs
        if log["time_taken"] > avg_time
    ]

    if not slower_steps:
        return "The child completed all steps smoothly today 😊"

    # Use Azure Language to polish wording
    text = (
        "The child took longer on these steps: "
        + ", ".join(slower_steps)
    )

    response = client.analyze_sentiment([text])[0]

    tone = "neutral"
    if response.sentiment == "negative":
        tone = "challenging"
    elif response.sentiment == "positive":
        tone = "comfortable"

    return (
        f"The child needed more time on: {', '.join(slower_steps)}. "
        f"Overall, these steps seemed {tone} today."
    )
