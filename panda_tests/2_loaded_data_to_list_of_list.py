# coding: utf-8

def main():
    data_to_save = []
    for hit in hits:
        curr = []
        curr.append(hit["_source"]["source"])
        curr.append(hit["_source"]["pictures"])
        data_to_save.append(curr)
    return data_to_save


if __name__ == '__main__':
    main()
