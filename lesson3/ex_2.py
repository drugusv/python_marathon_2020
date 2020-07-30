#virifca daca un text este palindrom

text = input("Introduceti textul: ")
rev_text = reversed(text)

if list(text) == list(rev_text):
   print("Textul este palindrome.")
else:
   print("Textul nu este palindrome.")