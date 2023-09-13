import collections
import itertools
import math

DIGITS_USED_IN_CODE = 6
CODE_LENGTH = 4
KNUTH_GUESS = (1, 1, 2, 2)
FOUR_PLUS_SIGNS = ['+', '+', '+', '+']

digits = tuple(range(DIGITS_USED_IN_CODE))
all_codes = set(itertools.product(digits, repeat=CODE_LENGTH))
set_of_all_codes= all_codes
set_of_possible_secrets = all_codes
guesses_made = 0


def print_set_size(s):
  print(f'Size of the set of possible guesses: {len(s)}')


def is_valid_secret(s):
  length = len(s)
  secret = int(s)
  if not (length == 4 and secret in range(1111, 6667)):
    print('invalid secret code')
  else:
    return True


def convert_to_tuple_of_ints(secret_code):
  secret_code = tuple(map(int, list(secret_code)))
  return secret_code


def get_all_codes(DIGITS_USED_IN_CODE):
  digits = tuple(range(DIGITS_USED_IN_CODE))
  all_codes = set(itertools.product(digits, repeat=CODE_LENGTH))
  return all_codes


def get_feedback(guess, secret_code):
  feedback = []
  guesses_remaining = []
  secret_code_remaining = []
  if guess == secret_code:
    feedback = FOUR_PLUS_SIGNS
    #print(feedback)
  else:
    for guess, secret in zip(guess, secret_code):
      if guess == secret:
        feedback.append('+')
      else:
        guesses_remaining.append(guess)
        secret_code_remaining.append(secret)
    for guess in guesses_remaining:
      if guess in secret_code_remaining:
        feedback.append('-')
        secret_code_remaining.remove(guess)
      else:
        feedback.append(' ')
  return feedback


def rmv(guess, secret_code, set_of_possible_secrets):
  for possible_guess in set_of_possible_secrets.copy():
    if set(get_feedback(possible_guess, secret_code)) != set(
        get_feedback(guess, secret_code)):
      set_of_possible_secrets.remove(possible_guess)
      #print(get_feedback(guess, secret_code))


def make_feedback_dict():
  '''
  Stores the feedback for each possible guess/code pair.
  '''
  feedback_dict = collections.defaultdict(dict)
  for guess, secret_code in itertools.product(all_codes, repeat=2):
    feedback_dict[guess][secret_code] = get_feedback(guess, secret_code)
  return feedback_dict
