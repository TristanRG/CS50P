import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))"', s)
    if match:
        video_id = match.group(2)
        return f"https://youtu.be/{video_id}"
    return None




if __name__ == "__main__":
    main()
