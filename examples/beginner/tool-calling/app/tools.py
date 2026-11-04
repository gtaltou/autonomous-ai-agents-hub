from agents import function_tool


def calculate(expression: str) -> str:
    """
    Pure Python function.
    """

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {},
        )

        return str(result)

    except (
    ValueError,
    TypeError,
    ZeroDivisionError,
    SyntaxError,
    NameError,
) as error:
        return f"Calculation error: {error}"


@function_tool
def calculator(
    expression: str,
) -> str:
    """
    Tool exposed to the Agent SDK.
    """

    return calculate(expression)