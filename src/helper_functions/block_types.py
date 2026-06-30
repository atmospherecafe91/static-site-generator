from enum import Enum

class BlockTypes(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'u_list'
    ORDERED_LIST = 'o_list'

def block_to_block_type_fn(markdown_txt: str) -> BlockTypes:

    split_markdown = markdown_txt.split('\n')

    if markdown_txt.startswith(('#', '##', '###', '####', '#####', '######')):
        return BlockTypes.HEADING
    elif split_markdown[0].startswith('```') and split_markdown[-1].startswith('```'):
        return BlockTypes.CODE
    elif markdown_txt.startswith('>'):
        for line in split_markdown:
            if not line.startswith('>'):
                return BlockTypes.PARAGRAPH
        return BlockTypes.QUOTE
    elif markdown_txt.startswith('- '):
        for lines in split_markdown:
            if not lines.startswith('- '):
                return BlockTypes.PARAGRAPH
        return BlockTypes.UNORDERED_LIST
    elif markdown_txt.startswith('1. '):
        i = 1

        for lines in split_markdown:
            if not lines.startswith(f'{i}. '):
                return BlockTypes.PARAGRAPH
            i += 1
        return BlockTypes.ORDERED_LIST
   
    
    return BlockTypes.PARAGRAPH
    
