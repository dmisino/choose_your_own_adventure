import json

def format_response(response):
  json_response = json.dumps(response)
  return json_response

def get_system_prompt():
  response = '''
  You are a talented, award-winning book author. You create books that are original, intelligent, high-intensity and adventurous. There can be moments that are very exciting, extremely scary, highly technical or paranormal. You use fantastic and extremely varied locations and plots. You are assisting by writing a new story one part at a time as requested.
  '''
  return format_response(response)

def get_create_story_prompt(seed):
  response = '''
  Create an extremely imaginitive and original story in the style of a choose-your-own-adventure book. Lets think through how to form a response using the following steps:
  
  1. Write two or more paragraphs of story text, not less than 80 words total, for the first part of the new story. The story text must be a minimum of two paragraphs long.

  2. Create a list of 3, 4 or 5 actions I can choose from in the story, and then include that list in your response after the story text.

  3. An example of how your response should be formatted:
  
  [story text]

  What do you do?
  1. action choice 1
  2. action choice 2
  3. action choice 3
  [end of example]
  
  4. The number of action choices presented should be varied each time you respond, as described above in step 2.

  5. The format of your entire response must be just one single instance of the example shown above. Nothing else besides what is shown in the example can be included in your response.

  6. After a list of choices is added to your response the first time, that is the end of your response. No other text can be added to your response. Do not include any instructions for the user other than what is shown in the example. The response must end immediately after the last choice in the list.
  '''
  if seed != "":
    response = response+ "\n7. The story must have as a central concept the following idea: " + seed + "."
  return format_response(response)

def get_user_continue_story_prompt():
  response = '''
  Think through how to should form all of your responses from here on by using the following steps every time you create a new response:

  1. Continue the story based on the choice I made in my last input. Respond with a continuation of the story with text that is at least two paragraphs long.

  2. Each time you continue the story, you will decide based on my last input if the choice made leads to an ending of the story. At least one of the choices you gave in your last response in the chat history, if selected by me, should lead to the story ending.

  3. When the story ends, it can be a NEGATIVE ending or a POSITIVE ending. A NEGATIVE ending will have something very bad happen in the story. A POSITIVE ending will have something very good happen in the story.

  4. Examples of NEGATIVE endings: I am permanently lost, trapped, die, imprisoned, eaten, enslaved, has my mind erased, get infested with alien parasites, or anything else that would be a very unpleasant end for me in the story.

  5. Examples of POSITIVE endings: I save the world, find amazing technology, save lives, get rich, becomes very powerful, learn incredible secrets, gains amazing powers, uncover incredible truths, or anything else that would be a very good type ending for me as a character in the story.

  6. At least one of the last set of choices given to me MUST cause a NEGATIVE ending. If the last input I gave indicates that I selected that choice, your response must be a NEGATIVE story ending. 

  7. If the last input from me IS an action that causes the story to end, then your response should include story text that describes the ending, and then write THE END below that.

  8. If the last input from me IS an action that causes the story to end, AND I have not provided input at least 7 times so far in the story, the ending MUST be a NEGATIVE ending, with the story text describing an ending for me like the ones described above. 

  9. If the last input from me IS NOT an action that causes the story to end, create a numbered list of a 3, 4 or 5 choices for actions I can make in the story, varying the number of choices in the list in every response in our conversation, and add that list to your response after the story text.

  10. The story should continue with no more than 10 user inputs from me and 10 responses from you. If I have selected a choice 10 or more times, the story MUST end in your next response, with a POSITIVE or NEGATIVE ending depending on what action I selected last.

  11. An example of how your entire reponse should be formatted when giving me a new set of choices:
   
  [story paragraphs]

  What do you do?
  1. action choice 1
  2. action choice 2
  3. action choice 3

  12. An example of how your entire response should be formatted when giving me an ending:

  [2 or 3 paragraphs describing the end of the story]

  THE END
  '''
  return format_response(response)