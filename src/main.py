from textnode import TextNode, TextType

def main():
    textNode = TextNode("This is some achor text", TextType.LINKS, "https://www.boot.dev")
    print(textNode)
if __name__=="__main__":
    main()