import os

def extract_numbers(data):
  nums = []
  for line in data:
    cols = line.split(' ')
    nums.append(int(cols[0]))

  nums.sort()
  return nums

def staircase_last_nums(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[step - 1])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

def extract_words(nums, words):
  message = ""
  for num in nums:
    for word in words:
      extracted_word = word.split(" ")
      number = int(extracted_word[0])
      if num == number:
        message += extracted_word[1]

  message = str.join(" ", message.splitlines())
  return message

def decode(message_file):
  if os.path.isfile(message_file):
    if os.stat(message_file).st_size == 0:
      print("File is empty.")
    else:
      file = open(message_file)
      data = file.readlines()

      all_nums = extract_numbers(data)
      final_nums = staircase_last_nums(all_nums)
      message = extract_words(final_nums, data)
      
      file.close()
      print(message)
      return message
  else:
    print("File not found.")

decode("message_file.txt")