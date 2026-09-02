import streamlit as st
from src.pipeline import run_research_pipeline
import time

# ======================
# Page Config
# ======================
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# Custom CSS
# ======================
st.markdown("""
<style>
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.3);
    }
    .report-box {
        background-color: #F8FAFC;
        border-left: 5px solid #4F46E5;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    .critique-box {
        background-color: #FFF7ED;
        border-left: 5px solid #F97316;
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ======================
# Sidebar
# ======================
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("---")
    
    st.markdown("### About")
    st.info("""
    This is a **Multi-Agent Research System** powered by:
    
    - 🔍 Search Agent
    - 📖 Read/Scrape Agent  
    - ✍️ Writer Agent
    - 🧐 Critic Agent
    """)
    
    st.markdown("---")
    st.markdown("### Example Topics")
    example_topics = [
        "Latest Nepal Floods News",
        "Impact of AI on Education 2026",
        "Electric Vehicles Market Trends",
        "Climate Change Policies in South Asia",
        "Rise of Quantum Computing"
    ]
    
    for topic in example_topics:
        if st.button(topic, use_container_width=True):
            st.session_state.topic_input = topic

# ======================
# Main Content
# ======================
st.markdown('<div class="main-title">🧠 Multi-Agent Research System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter any topic and let the agents research, write & critique a full report for you.</div>', unsafe_allow_html=True)

# Topic Input
topic = st.text_input(
    "Research Topic",
    value=st.session_state.get("topic_input", ""),
    placeholder="e.g. Latest developments in AI Agents, Nepal Floods, etc.",
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns([1, 1, 3])
with col1:
    run_button = st.button("🚀 Start Research", use_container_width=True)
with col2:
    clear_button = st.button("🗑️ Clear", use_container_width=True)

if clear_button:
    st.session_state.clear()
    st.rerun()

# ======================
# Run Pipeline
# ======================
if run_button:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        with st.status("Agents are working...", expanded=True) as status:
            st.write("🔍 Search Agent is gathering information...")
            time.sleep(0.5)
            
            try:
                result = run_research_pipeline(topic)
                
                st.write("📖 Read Agent finished extracting content...")
                st.write("✍️ Writer Agent is generating the report...")
                st.write("🧐 Critic Agent is reviewing the report...")
                
                status.update(label="✅ Research Completed!", state="complete", expanded=False)
                
                # Store in session state
                st.session_state.result = result
                st.session_state.topic = topic
                
            except Exception as e:
                status.update(label="❌ Error occurred", state="error")
                st.error(f"Something went wrong: {str(e)}")
                st.stop()

# ======================
# Display Results
# ======================
if "result" in st.session_state:
    result = st.session_state.result
    topic = st.session_state.topic
    
    st.markdown("---")
    st.subheader(f"📄 Research Report: {topic}")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📝 Final Report", "🧐 Critique", "📊 Raw Data"])
    
    with tab1:
        st.markdown(result.get("final_report", "No report generated."))
        
        # Download button
        st.download_button(
            label="⬇️ Download Report as Markdown",
            data=result.get("final_report", ""),
            file_name=f"research_report_{topic[:30].replace(' ', '_')}.md",
            mime="text/markdown"
        )
    
    with tab2:
        st.markdown(result.get("critique", "No critique generated."))
    
    with tab3:
        st.write("**Search Results:**")
        st.text(result.get("search_results", "")[:2000])
        
        st.write("**Scraped Content:**")
        st.text(result.get("scraped_content", "")[:2000])

# Footer
st.markdown("---")
st.caption("Built with LangChain + Groq + Streamlit • Multi-Agent Research System")