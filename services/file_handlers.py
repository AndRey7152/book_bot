import logging
import os


logger = logging.getLogger(__name__)

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    zn = ['.', ',', '!', '?', ':', ';']
    page_text = text[start:start + size]
    page_size = len(page_text)
    
    if len(text) > start + size:
        while start+size != len(text) and text[start+size] != ' ':
            size -= 1

        word_li = text[start:start + size].split(' ')
        for i in word_li[::-1]:
            if sum(res in zn for res in i) == 1:
                break
            word_li.pop()
        
        page_text = ' '.join(word_li).rstrip()
        page_size = len(page_text)
    
    return page_text, page_size

def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        count = 1
        while len(text) != 0:
            txt = _get_part_text(text, 0, page_size)
            book[count]= txt[0].lstrip()
            text = text[txt[1]:]
            count += 1    
    return book

print(prepare_book('book/book.txt'))
