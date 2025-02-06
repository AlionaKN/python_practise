from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    unique_list = []

    for i in str_list:
        if i not in unique_list:
            unique_list.append(i)

    unique_list.sort()

    return unique_list

