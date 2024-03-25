from services.db import *
from scan import main
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some chars.')
    parser.add_argument('annotation', type=str, help='an annotation for the script')

    args = parser.parse_args()

    main(args.annotation)