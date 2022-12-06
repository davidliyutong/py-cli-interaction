from typing import Tuple, Optional, Union, List

from rich.console import Console


def parse_cli_string(msg, default_value: str = None) -> Tuple[Optional[str], Optional[Exception]]:
    console = Console()
    string_input = console.input(
        " > " + msg + f" [ default={default_value} ]:"
    )

    if string_input == '':
        if default_value is not None:
            return default_value, None
        else:
            return None, ValueError(f"empty input")
    else:
        return string_input, None


def must_parse_cli_string(msg: str, default_value: str = None) -> str:
    console = Console()
    while True:
        ret, err = parse_cli_string(msg, default_value)
        if err is None:
            return ret
        else:
            console.log(err)


def parse_cli_bool(msg: str,
                   default_value: bool = None) -> Tuple[Optional[bool], Optional[Exception]]:
    console = Console()
    string_input = console.input(
        " > " + msg +
        f" [ {'Y' if default_value == True else 'y'}/{'N' if default_value == False else 'n'} ]:"
    )
    if string_input in ['Y', 'y', 'yes']:
        return True, None
    elif string_input in ['N', 'n', 'no']:
        return False, None
    elif string_input == '':
        if default_value is not None:
            return default_value, None
        else:
            return None, ValueError(f"{string_input} is invalid input")
    else:
        return None, ValueError(f"{string_input} is invalid input")


def must_parse_cli_bool(msg: str,
                        default_value: bool = None) -> bool:
    console = Console()
    while True:
        ret, err = parse_cli_bool(msg, default_value)
        if err is None:
            return ret
        else:
            console.log(err)


def parse_cli_int(msg: str,
                  min: int = None,
                  max: int = None,
                  default_value: int = None) -> Tuple[Optional[int], Optional[Exception]]:
    console = Console()

    string_input = console.input(
        " > " +
        msg +
        f" [ default={default_value} ]:"
    )

    if string_input == '' and default_value is not None:
        sel = default_value
        return sel, None
    else:
        try:
            sel = int(string_input)
            if (min is not None and max is not None) and (sel < min or sel > max):
                return None, ValueError(f"{sel} is out of range")
            else:
                return sel, None

        except Exception as e:
            return None, e


def must_parse_cli_int(msg: str,
                       min: int = None,
                       max: int = None,
                       default_value: int = None) -> int:
    console = Console()
    while True:
        ret, err = parse_cli_int(msg, min, max, default_value)
        if err is None:
            return ret
        else:
            console.log(err)


def parse_cli_float(msg: str,
                    min: float = None,
                    max: float = None,
                    default_value: float = None) -> Tuple[Optional[int], Optional[Exception]]:
    console = Console()

    string_input = console.input(
        " > " +
        msg +
        f" [ default={default_value} ]:"
    )

    if string_input == '' and default_value is not None:
        sel = default_value
        return sel, None
    else:
        try:
            sel = float(string_input)
            if (min is not None and max is not None) and (sel < min or sel > max):
                return None, ValueError(f"{sel} is out of range")
            else:
                return sel, None

        except Exception as e:
            return None, e


def must_parse_cli_float(msg: str,
                         min: float = None,
                         max: float = None,
                         default_value: float = None) -> int:
    console = Console()
    while True:
        ret, err = parse_cli_float(msg, min, max, default_value)
        if err is None:
            return ret
        else:
            console.log(err)


def parse_cli_sel(msg: str,
                  candidates: Union[Tuple[object], List[object]],
                  min: int = 0,
                  max: int = None,
                  default_value: int = None) -> Tuple[Optional[int], Optional[Exception]]:
    console = Console()

    if max is None:
        max = len(candidates) + min - 1

    string_input = console.input(
        " > " +
        msg +
        f" [ {min}-{max}, default={default_value} ]:\n" +
        "\n".join(["\t" + str(idx + min) + " - " + str(item) for idx, item in enumerate(candidates)]) +
        "\n > "
    )

    if string_input == '' and default_value is not None:
        sel = default_value
        return sel, None
    else:
        try:
            sel = int(string_input)
        except Exception as e:
            return None, e

        if sel < min or sel > max:
            return None, ValueError(f"{sel} is out of range")

        return sel, None


def must_parse_cli_sel(msg: str,
                       candidates: Union[Tuple[object], List[object]],
                       min: int = 0,
                       max: int = None,
                       default_value: int = None) -> int:
    console = Console()
    while True:
        ret, err = parse_cli_sel(msg, candidates, min, max, default_value)
        if err is None:
            return ret
        else:
            console.log(err)
