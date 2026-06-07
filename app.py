import os
import streamlit as st
from dotenv import load_dotenv
import autogen

# 1. UI Setup: Page Config
st.set_page_config(page_title="AI Auditor Pro", page_icon="🛡️", layout="centered")
st.title("🛡️ Enterprise AI Expense Auditor")
st.markdown("Upload a text file containing the expense report, and our AI agent team will audit it instantly.")

# 2. Credentials & Config Load
load_dotenv()
config_list = [{
    "model": os.environ.get("MODEL_NAME"),
    "api_key": os.environ.get("GITHUB_TOKEN"),
    "base_url": os.environ.get("AI_ENDPOINT"),
}]
llm_config = {"config_list": config_list, "temperature": 0.2}

# 3. File Uploader UI
uploaded_file = st.file_uploader("Upload Expense Report (.txt)", type=["txt"])

if uploaded_file is not None:
    # File read karna
    document_content = uploaded_file.read().decode("utf-8")
    
    with st.expander("📄 View Uploaded Document"):
        st.text(document_content)
        
    # Button for running audit
    if st.button("🚀 Run AI Audit", type="primary"):
        with st.spinner("👔 Assembling the Audit Team and Analyzing..."):
            
            # --- AGENT SETUP ---
            finance_auditor = autogen.AssistantAgent(
                name="Finance_Auditor",
                system_message="You are a strict Financial Auditor. Analyze expenses for fraud. Explain in 2 sentences. End with 'Passing to Compliance_Officer'.",
                llm_config=llm_config,
            )

            compliance_officer = autogen.AssistantAgent(
                name="Compliance_Officer",
                system_message="You are the Chief Compliance Officer. Review findings. If it violates policy, clearly REJECT it. Give a reason, and ALWAYS end with 'TERMINATE'.",
                llm_config=llm_config,
            )

            admin = autogen.UserProxyAgent(
                name="Admin",
                human_input_mode="NEVER",
                is_termination_msg=lambda x: x.get("content", "") and "TERMINATE" in x.get("content", ""),
                code_execution_config=False,
            )

            groupchat = autogen.GroupChat(
                agents=[admin, finance_auditor, compliance_officer], 
                messages=[], 
                max_round=5,
                speaker_selection_method="auto"
            )
            manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

            task_description = f"Please audit the following expense report:\n\n{document_content}"

            # --- RUN CHAT ---
            chat_result = admin.initiate_chat(manager, message=task_description)
            
            # --- DISPLAY RESULTS IN UI ---
            st.success("✅ Audit Complete!")
            st.subheader("💬 Agent Conversation Log")
            
            # Extract and display chat history on UI
            for msg in chat_result.chat_history:
                if msg["name"] != "Admin": # Admin ka prompt dubara nahi dikhana
                    with st.chat_message("assistant"):
                        # FIX: Dollar sign ko escape karna taaki UI na bigde
                        safe_content = msg['content'].replace('$', '\\$')
                        st.markdown(f"**{msg['name']}**:\n\n{safe_content}")