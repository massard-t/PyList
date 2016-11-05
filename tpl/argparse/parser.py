def prep_my_parser(args):
    parser = argparse.ArgumentParser()
    group0 = parser.add_mutually_exclusive_group()
    group0.add_argument('-i', '--ip')
    group0.add_argument('-n', '--name')
    parser.add_argument('--input_file')