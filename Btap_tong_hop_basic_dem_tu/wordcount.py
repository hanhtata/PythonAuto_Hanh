#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Quang Le - Techmaster.vn - 09/2021
########

"""Wordcount exercise

Hàm main() đã được định nghĩa hoàn chỉnh ở dưới. Bạn phải viết hàm print_words()
và print_top() mà sẽ được gọi từ main().

1. Với đối số --count, viết hàm print_words(filename) đếm số lần xuất hiện của mỗi từ 
trong file đầu vào và in ra theo định dạng sau:
word1 count1
word2 count2
...

In danh sách trên theo thứ tự từ điển các từ (python sẽ sắp xếp dấu câu đứng trước
các chữ cái nên cũng không thành vấn đề). Lưu tất cả các từ dưới dạng chữ thường,
vì vậy 'The' và 'the' được tính là cùng một từ.

2. Với đối số --topcount, viết hàm print_top(filename) tương tự như print_words()
nhưng chỉ in ra 20 từ thông dụng nhất sắp xếp theo từ thông dụng nhất ở trên cùng.

Tùy chọn: định nghĩa một hàm helper để tránh lặp lại code trong các hàm 
print_words() và print_top().

"""

import sys

# +++your code here+++
def helper(filename):
  contents = ""
  with open(filename, 'r') as file_again:
      for i in file_again:
          contents+= i.replace(".","").replace(",","").replace("?","").replace("!","").replace("-","").replace(":","").replace('"','')
      content = contents.split()
      for i in range(len(content)) :
        content[i]= content[i].lower()
  return(content)
def print_words(filename):
  content = helper(filename)
  result = []
  for i in content:
    result.append(i+" "+str(content.count(i)))
  result1= set(result)
  result= list(result1)
  result.sort()
  for i in result:
    print(i)

def print_top(filename):
  content = helper(filename)
  result ={}
  for i in content:
    result[i]=str(content.count(i))
  list1=list(result.values())
  for i in range(len(list1)):
    list1[i]=int(list1[i])
  list1= sorted(list1)[-20:-1]
  list2=[]
  for j in list1:
    for i in list(result.keys()):
      if  int(result[i]) == j:
        if(i not in list2):
          list2.append(i)
          break;
  for i in range(len(list2)):
    print(list2[i]+ " " +str(list1[i]))
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()