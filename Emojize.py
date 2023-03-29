import emoji

def main():
    emo = input("Emoji: ")
    if emoji.is_emoji(checkEmoji(emo)):
        print(f"Output:{emoji.emojize(emo)}")
    else:
        print("Yor text is not emoji")

def checkEmoji(txt):
    return emoji.emojize(txt)

if __name__ == "__main__":
    main()
