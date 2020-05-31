import re

# These are the emails you will be censoring. The open() function is opening the text file that the emails are
# contained in and the .read() method is allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Email One

def censor_words(email, words):

  asterisk = []
  while len(asterisk) < len(words):
    asterisk.append('*')
  asterisk_join = ''.join(asterisk)
  new_email = email.replace(words, asterisk_join)

  return new_email

print(censor_words(email_one, 'learning algorithms'))


# Email Two

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation",
                     "learning algorithm", "her", "herself"]

def censor_lst(email, lst):
  update_email = ''
  i = 0
  for item in lst:
    stars = []
    while len(stars) < len(item):
      stars.append('*')
    stars_join = ''.join(stars)

    if i == 0:
      regex =  "\\b"+ item + "\\b"
      update_email = re.sub(regex, stars_join, email, flags = re.IGNORECASE)

      i += 1
    else:
      regex =  "\\b"+ item + "\\b"
      update_email = re.sub(regex, stars_join, update_email, re.IGNORECASE)


  return update_email

print(censor_lst(email_two, proprietary_terms))


#Email Three

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]

def negative_proprietary_censor(email, lst1, lst2):

  update_email = ''
  i = 0
  k = 0

  for item in lst1:

    stars = []
    while len(stars) < len(item):
      stars.append('*')
    stars_join = ''.join(stars)

    string_item = str(item)
    regex =  "\\b"+ item + "\\b"
    tmp_lst = re.search(regex, email)
    if tmp_lst != None:
      i += 1
    if i >= 2:
      break


  for word in lst1:
    if i >=2 and k == 0 :
      regex = "\\b"+ word + "\\b"
      update_email = re.sub(regex, stars_join, email, flags = re.IGNORECASE)
      k += 1

    elif i >= 2 and k != 0:
      regex = "\\b"+ word + "\\b"
      update_email = re.sub(regex, stars_join, update_email, flags = re.IGNORECASE)

  update_email = censor_lst(update_email, lst2)
  return update_email

print(negative_proprietary_censor(email_three, negative_words,proprietary_terms))


#Email Four

def censor_it_all(email, lst1, lst2):
  censor_email = negative_proprietary_censor(email,lst1,lst2)
  split_email = censor_email.split(' ')
  new_split_email = []
  i = 0
  k = 0
  try:
    for word in split_email:

      if k < i:
        k += 1
        continue

      else:
        tmp_value1 = word.find('*')
        tmp_value2 = word.find('\n')
        if tmp_value1 == -1:
          if split_email[i + 1].find('*') != -1 :
            stars = []
            while len(stars) < len(word):
              stars.append('*')
            stars_join = ''.join(stars)
            new_split_email.append(stars_join)
            i += 1
            k += 1
          else:
            new_split_email.append(word)
            i += 1
            k += 1
        else:
          if tmp_value2 == -1:
            if split_email[i +1].find('*') == -1 :
              stars = []
              while len(stars) < len(split_email[i + 1]):
                stars.append('*')
              stars_join = ''.join(stars)
              new_split_email.append(word)
              new_split_email.append(stars_join)
              i += 2
              k += 1
            else:
              new_split_email.append(word)
              i += 1
              k += 1
          else:
            new_split_email.append(word)
            i += 1
            k += 1

  except IndexError:
    new_join_email = ' '.join(new_split_email)
    return new_join_email

print(censor_it_all(email_four,negative_words,proprietary_terms))
