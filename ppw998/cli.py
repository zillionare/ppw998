"""Console script for ppw998."""

import fire


def help() -> None:
    print("ppw998")
    print("=" * len("ppw998"))
    print("Skeleton project created by Python Project Wizard (ppw)")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
