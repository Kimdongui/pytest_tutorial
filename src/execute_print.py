import argparse


def get_greeting_string(group : str) -> str:
    return f"Hello {group}, nice to meet you!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="pytest tutorial...")
    parser.add_argument("--group_name", type=str, help="A group name to meet")
    args =parser.parse_args()

    greet_string=get_greeting_string(args.group_name)
    print(greet_string)