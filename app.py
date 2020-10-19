print("Title of program: Study motivation bot")
print()
while True:
  description = input("Why do you not want to study?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("you can always take a break")
      counter += 1
    if each_word == "lazy":
      feelings_list.append("lazy")
      encouragement_list.append("you have set goals for yourself and do not want to disappoint yourself")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you can always take a short nap so you would feel more refreshed and motivated to study later")
      counter += 1
    if each_word == "unmotivated":
      feelings_list.append("unmotivated")
      encouragement_list.append("you can grab something to eat or watch a video, and promise yourself that you will study afterwards")
      counter += 1    
    if each_word == "unwell":
      feelings_list.append("unwell")
      encouragement_list.append("your health comes first, so take a rest")
      counter += 1
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel more motivated :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
