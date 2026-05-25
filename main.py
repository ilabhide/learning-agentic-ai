print("=== VERIFYING XAI GROK ENVIRONMENT ===")

try:
    import xai_sdk
    print(f"✅ Official xai-sdk is successfully installed! (Version: {xai_sdk.__version__})")
except ImportError:
    print(f"Official xai-sdk not found. Run pip install xai-sdk' in your terminal")

try:
    import openai
    print(f"OpenAI compatibility library is installed! (Version: {openai.__version__})")
except ImportError:
    print(f"OpenAI library not found. Run 'pip install openai' to use it")





print("=======================================")
