def markdown_to_blocks(markdown_txt: str) -> list[str]:
    
    return list(filter(lambda x: x != '', map(lambda x: x.strip(), markdown_txt.split('\n\n'))))
