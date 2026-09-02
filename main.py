from src.pipeline import run_research_pipeline

topic = "Latest Nepal Floods News"

result = run_research_pipeline(topic)

print("\n" + "="*60)
print("FINAL RESEARCH REPORT")
print("="*60)
print(result["final_report"])

print("\n" + "="*60)
print("CRITIQUE / FEEDBACK")
print("="*60)
print(result["critique"])