def solution(string, ending):
    # your code here...
    len_end = len(ending)*(-1)
    if(string[len_end:] == ending or ending == ''):
        return True
    if(string[len_end:] != ending):
        return False

#easy shorter solution i found
def solution(string, ending):
    return string.endswith(ending)