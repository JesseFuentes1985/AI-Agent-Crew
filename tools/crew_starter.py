"""
crew_starter.py — crewAI starter template for Orbit's agent crew

Venv: /Users/jessefuentes/.openclaw/workspace-main/.venv-crew (Python 3.11)
Run:  source .venv-crew/bin/activate && python tools/crew_starter.py

Uses Ollama locally — no API keys needed.
Models: mistral (fast), nous-hermes2 (smart), llava (vision)
"""

from crewai import Agent, Task, Crew, Process

# ─────────────────────────────────────────────
# AGENTS
# ─────────────────────────────────────────────

researcher = Agent(
    role="Researcher",
    goal="Find, analyze, and summarize key information accurately",
    backstory=(
        "A meticulous researcher who digs deep into topics, "
        "cross-references sources, and presents clear, concise findings."
    ),
    verbose=True,
    llm="ollama/mistral",           # swap to ollama/nous-hermes2 for deeper reasoning
)

writer = Agent(
    role="Writer",
    goal="Turn research into clear, engaging written content",
    backstory=(
        "A skilled communicator who takes raw research and shapes it "
        "into polished, readable output tailored to the audience."
    ),
    verbose=True,
    llm="ollama/mistral",
)

# ─────────────────────────────────────────────
# TASKS
# ─────────────────────────────────────────────

research_task = Task(
    description=(
        "Research the top 3 benefits of running AI agents locally "
        "(on-device with Ollama) versus using cloud APIs. "
        "Focus on: privacy, cost, and latency."
    ),
    expected_output=(
        "A structured list of 3 benefits with a 1-2 sentence explanation each."
    ),
    agent=researcher,
)

write_task = Task(
    description=(
        "Using the researcher's findings, write a short 3-paragraph summary "
        "explaining why local AI agents are powerful. "
        "Keep it punchy and accessible."
    ),
    expected_output=(
        "3 short paragraphs, each covering one benefit. "
        "Conversational tone, no jargon."
    ),
    agent=writer,
    context=[research_task],        # writer sees researcher's output
)

# ─────────────────────────────────────────────
# CREW
# ─────────────────────────────────────────────

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,     # researcher goes first, writer follows
    verbose=True,
)

# ─────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n🚀 Launching crew...\n")
    result = crew.kickoff()
    print("\n" + "="*60)
    print("✅ CREW OUTPUT")
    print("="*60)
    print(result)
