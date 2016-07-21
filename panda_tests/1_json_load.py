# coding: utf-8
import json


def main():
    with open("09ff.json", 'r') as f:
        f_content = f.read()
    content_json = json.loads(f_content)
    return content_json


if __name__ == '__main__':
    main()
