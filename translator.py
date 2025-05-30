from translate import Translator

def main():
    print("🌍 Welcome to the Language Translator Tool!")
    print("🔤 Example language codes: fr (French), es (Spanish), hi (Hindi), ta (Tamil), de (German)")
    
    while True:
        # Get the target language from user
        to_lang = input("👉 Enter the language code to translate to (or type 'exit' to quit): ").strip()
        if to_lang.lower() == "exit":
            print("👋 Bye! Have a great day!")
            break

        # Get the text to translate
        text = input("📝 Enter the text to translate: ").strip()

        try:
            translator = Translator(to_lang=to_lang)
            translation = translator.translate(text)
            print(f"✅ Translated ({to_lang}): {translation}\n")
        except Exception as e:
            print("❌ Oops! Something went wrong. Please try again.")
            print("Error:", str(e))
            print()

if __name__ == "__main__":
    main()
