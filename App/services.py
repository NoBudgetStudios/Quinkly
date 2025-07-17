import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from models import PromptInput

# =========================
#  ENVIRONMENT SETUP
# =========================

def load_env_variables():
    load_dotenv()
    return {
        "provider": os.getenv("LLM_PROVIDER", "openai").lower(),
        "openrouter_api_key": os.getenv("OPENROUTER_API_KEY")
    }

# =========================
#  LLM INITIALIZATION
# =========================

def init_llm(provider: str, api_key: str):
    if provider == "openai":
        return ChatOpenAI(
            temperature=0.7,
            model_name="mistralai/mixtral-8x7b-instruct",
            openai_api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
    else:
        raise ValueError("❌ Unsupported LLM provider. Use 'openai' only for now.")

# =========================
#  PROMPT CONSTRUCTION
# =========================

def build_prompt(data: PromptInput) -> str:
    return (
        f"Write a {data.output_type} about '{data.topic}' "
        f"in a {data.tone} tone and {data.style} style. "
        f"Include the following keywords: {', '.join(data.keywords)}."
    )

# =========================
#  RESPONSE GENERATION
# =========================

def generate_content(data: PromptInput) -> str:
    config = load_env_variables()
    llm = init_llm(config["provider"], config["openrouter_api_key"])
    prompt = build_prompt(data)

    try:
        if config["provider"] == "openai":
            # Uncomment the following lines to activate credit-burning
            response = llm.invoke([HumanMessage(content=prompt)])
            print("[OpenAI response]", response)
            return response.content
            #return "Uncomment so you start burn credits!"
        else:
            return "This code only supports OpenRouter via 'openai' provider."
    except Exception as e:
        print(f"[Error] {e}")
        return f"Error: {e}"
