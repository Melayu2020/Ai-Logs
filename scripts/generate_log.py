import os
from datetime import datetime

# Generate a Markdown AI Log
log_content = """# AI Log - {}
**AI Tool:** ChatGPT  
**Key Insight:** AI-assisted project brainstorming  
**Source:** ChatGPT  
**Linked Projects:** Habit-Tracking App  
**Next Steps:** Validate market research with Perplexity  
**Tags:** #ResearchNeeded  
""".format(datetime.now().strftime("%Y-%m-%d"))

# Save log to 'logs/' folder
logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)
filename = f"{logs_dir}/{datetime.now().strftime('%Y-%m-%d')}-chatgpt.md"

with open(filename, "w") as file:
    file.write(log_content)

print(f"Generated AI Log: {filename}")
