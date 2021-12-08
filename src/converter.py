import argparse
import sys

# gui
from easygui import msgbox

# custom
from config import ROOT_DIR
from libs import th_handler
from libs.converter_func import convert_dict
from libs.logger import error_checker
from libs.manage_files import gen_files_dict


def main():
    parser = argparse.ArgumentParser(description="Convert gnlabs to kitti")
    parser.add_argument("--root_path", help="root path.", type=str, default=ROOT_DIR)
    parser.add_argument("--num_threads", help="no of thread.", type=int, default=3)
    args = parser.parse_args()

    print("validating data...")
    files_dict = gen_files_dict(args.root_path)

    for ext, convert_func in convert_dict.items():

        print(f"{ext} converting... ({args.num_threads} workers)")

        th_handler.run(
            (ext, convert_func),
            files_dict[ext],
            args.num_threads,
        )

        if error_checker():
            print("conversion error!")
            msgbox(error_checker())
            sys.exit()
    print("-----conversion has been finished-----")


if __name__ == "__main__":
    main()
