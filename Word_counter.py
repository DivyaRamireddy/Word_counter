# 📖 Word Counter for Text File

def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words), words
    except FileNotFoundError:
        print("❌ File not found! Please check the filename.")
        return 0, []


def main():
    print("📖 Welcome to Word Counter 📖")

    filename = input("Enter the filename (e.g., sample.txt): ")

    total_words, words = count_words(filename)

    if total_words > 0:
        print(f"\n✅ The file '{filename}' has {total_words} words.")
        show = input("Do you want to see the first 20 words? (y/n): ")
        if show.lower() == "y":
            print(" ".join(words[:20]))


if __name__ == "__main__":
    main()
