# -*- coding: utf-8 -*-
from os import stat
import re

# Hàm đọc dữ liệu từ điển đã xử lý
def get_list_dictionary(filename):
    with open(filename, 'r', encoding='utf-8') as reader:
        lines = [line.rstrip() for line in reader]
    return lines

# Hàm kiểm tra xem từ đầu vào có nằm trong từ điển hay không
def is_in_dictionary(input_word, dictionary):
    input_word = input_word.lower()
    input_word = input_word[:-1] if (input_word[len(input_word) - 1] == ',' or input_word[len(input_word) - 1] == '.' or input_word[len(input_word) - 1] == ':' or input_word[len(input_word) - 1] == '?' or input_word[len(input_word) - 1] == ';') else input_word
    for word in dictionary:
        if input_word == word:
            return True
    return False

# Hàm cắt câu thành các tiếng cách nhau bởi dấu khoảng trắng
def split_sentence(sentence):
    return sentence.split(' ')

pattern_01 = r"^[ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđa-zA-Z]*$"
# Regex địa chỉ website
pattern_02 = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
# Regex Số thập phân
pattern_03 = r"\d+[\,\.]\d+"
# Regex học hàm <A-Z>.<A-Z>.<space>
pattern_04 = r"GS.TS.|PGS.TS.|TS.|Ths."
# Regex cho ngày tháng năm
pattern_05 = r"^(?=\d)(?:(?:31(?!.(?:0?[2469]|11))|(?:30|29)(?!.0?2)|29(?=.0?2.(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00)))(?:\x20|$))|(?:2[0-8]|1\d|0?[1-9]))([-./])(?:1[012]|0?[1-9])\1(?:1[6-9]|[2-9]\d)?\d\d(?:(?=\x20\d)\x20|$))?(((0?[1-9]|1[012])(:[0-5]\d){0,2}(\x20[AP]M))|([01]\d|2[0-3])(:[0-5]\d){1,2})?$"
# Regex cho ký tự kết thúc câu
pattern_06 = r"\?|\.|\:|\!|\...|\"|\;"


def split_text_to_paragraph(text):
    pass

# Hàm cắt đoạn ra từng câu
def split_paragraph_to_sentence(line):
    arr = line.split(' ')
    list_sentence = []
    low = 0
    high = 0
    for item in arr:
        if ((not re.match(pattern_02, item) 
        and not re.match(pattern_03, item) 
        and not re.match(pattern_04, item) 
        and not re.match(pattern_05, item)) 
        and re.match(pattern_06, item[len(item)-1])):
            l = []
            for i in range(low, high + 1):
                l.append(arr[i])
            list_sentence.append(' '.join(l))
            low = high + 1
        high += 1
    return list_sentence

# Hàm thực thi maximum matching, với độ dài từ lớn nhất là 3
def maximum_matching(list_words):
    i = 0
    result = []
    while(i < len(list_words)):
        best = ''
        start = i
        if (is_in_dictionary(list_words[i], lst_dict) == True):
            best = list_words[i]
            # print(best)
        if (i + 1 < len(list_words)):
            if (is_in_dictionary(' '.join([list_words[i], list_words[i + 1]]), lst_dict) == True):
                best = ' '.join([list_words[i], list_words[i + 1]])
                # print(best)
                start = i + 1
        if (i + 2 < len(list_words)):
            if (is_in_dictionary(' '.join([list_words[i], list_words[i + 1], list_words[i + 2]]), lst_dict) == True):
                best = ' '.join([list_words[i], list_words[i + 1], list_words[i + 2]])
                # print(best)
                start = i + 2
        if best != '':
            # print(best)
            result.append(best.replace(' ', '_'))
        else:
            result.append(list_words[i])
        i = start + 1
    # print(' '.join(result))
    print(result)
    return ' '.join(result)


lst_dict = get_list_dictionary('./src/data/process_vdic.txt')

input_string_00 = "Ngày chủ nhật bố mẹ vắng nhà. Bé Thảo được dịp nô đùa thoả thích."
input_string_01 = "PGS.TS. Trần Văn A, hiện đang đi công tác ở Hà Nội. Ông ấy sẽ trở lại giảng dạy vào thứ 3 tuần sau. GS.TS. Hà đã nghỉ hưu. TS. Lê Ngọc Thành. Trang http://www.fit.hcmus.edu.vn là trang website của khoa CNTT KHTN. Số 123.456 là một số thực."
input_string_02 = "Hôm nay trời thật đẹp, Nam sẽ đi xem phim. Bộ phim bắt đầu vào 13:30 chiều."
input_string_03 = "Má nó! Thằng ranh con, nó vừa ăn trộm táo nhà tôi."
input_string_04 = "Ông Tuấn bảo rằng: Cứ làm như hướng dẫn là được!"
input_string_05 = "Ông già đi nhanh."
input_string_06 = "Bạn có bị ngốc không? Bạn nên kiểm tra lại cách làm này đi nhé!"

lst_sentences_00 = split_paragraph_to_sentence(input_string_00)
    
if __name__ == "__main__":
    result = []
    for sentence in lst_sentences_00:
        list_words = split_sentence(sentence)
        result.append(maximum_matching(list_words))
    print(result)
