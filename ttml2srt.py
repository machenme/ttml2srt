import argparse
import re


def ttml_to_srt(ttml_text):
    pattern = r'<p begin="(\d{2}:\d{2}:\d{2}.\d{3})" end="(\d{2}:\d{2}:\d{2}.\d{3})".*>(.*)<\/p>'
    result = ""
    for idx, sub in enumerate(ttml_text, start=1):
        matches = re.findall(pattern, sub)
        for match in matches:
            begin, end, srt_sub = match
            result += f"{idx}\n{begin} --> {end}\n{srt_sub}\n"
    result = result.replace(".", ",")
    return result


def main(input_file, output_file=None):
    with open(input_file, "r", encoding="utf-8") as f:
        subs = f.readlines()
    subs = [i for i in subs if "begin" in i]

    srt_content = ttml_to_srt(subs)

    if output_file is None:
        output_file = input_file.replace(".ttml", ".srt")

    with open(output_file, "w+", encoding="utf-8") as f:
        f.write(srt_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert TTML to SRT format")
    parser.add_argument("input_file", help="Input TTML file")
    parser.add_argument("-o", "--output_file", help="Output SRT file")
    args = parser.parse_args()

    main(args.input_file, args.output_file)
