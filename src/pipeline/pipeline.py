from src.agents.agents import (
    create_search_agent,
    create_read_agent,
    writer_chain,
    critic_chain
)


def run_research_pipeline(topic: str) -> dict:
    print(f"\n🚀 Starting research pipeline for topic: {topic}\n")
    state = {}

    # -------------------------
    # Step 1: Search Agent
    # -------------------------
    print("🔍 Search Agent working...")
    search_agent = create_search_agent()

    search_results = search_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"Search the web for the latest news about: {topic}. Return titles, links and short summaries."
            }
        ]
    })

    state["search_results"] = search_results["messages"][-1].content
    print("\n----- SEARCH RESULTS -----")
    print(state["search_results"][:1500])
    print("--------------------------\n")

    # -------------------------
    # Step 2: Read / Scrape Agent
    # -------------------------
    print("📖 Read Agent working...")
    read_agent = create_read_agent()

    read_results = read_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"From the following search results, extract the most important and detailed information about '{topic}':\n\n{state['search_results'][:3000]}"
            }
        ]
    })

    state["scraped_content"] = read_results["messages"][-1].content
    print("\n----- SCRAPED CONTENT -----")
    print(state["scraped_content"][:1500])
    print("---------------------------\n")

    # -------------------------
    # Step 3: Writer Chain
    # -------------------------
    print("✍️  Writer Agent working...")

    final_report = writer_chain.invoke({
        "topic": topic,
        "research": state["scraped_content"]
    })

    state["final_report"] = final_report
    print("\n----- FINAL REPORT -----")
    print(final_report[:2000] if final_report else "EMPTY REPORT")
    print("------------------------\n")

    # -------------------------
    # Step 4: Critic Chain
    # -------------------------
    print("🧐 Critic Agent working...")

    critique = critic_chain.invoke({
        "report": state["final_report"]
    })

    state["critique"] = critique

    print("🎉 Pipeline finished!\n")
    return state