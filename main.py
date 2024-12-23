import random

def choose_word(word_list):
  return random.choice(word_list)

def get_user_guess():
  guess = input("Enter your 5-letter guess: ")
  while len(guess) != 5:
      print("Please enter a 5-letter word.")
      guess = input("Enter your 5-letter guess: ")
  return guess

def provide_feedback(guess, target):
  feedback = []
  for i in range(5):
      if guess[i] == target[i]:
          feedback.append("🟩")
      elif guess[i] in target:
          feedback.append("🟨")
      else:
          feedback.append("⬜")
  return feedback

def play_game(word_list):
  target_word = choose_word(word_list)
  attempts = 6
  for _ in range(attempts):
      user_guess = get_user_guess()
      feedback = provide_feedback(user_guess, target_word)
      print("Feedback:", feedback)
      if user_guess == target_word:
          print("Congratulations! You guessed the word.")
          break
  else:
      print(f"Sorry, you've run out of attempts. The word was: {target_word}")

word_list = ["apple", "bread", "crane", "stone", "lemon"]
play_game(word_list)
