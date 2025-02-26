def markdown_to_blocks(markdown_text: str) -> list[str]:
    return list(
        filter(
            lambda y: y.strip() != "",
            (map(
                lambda x: x.strip().replace(" \n", ""),
                markdown_text.split("\n\n")))))
