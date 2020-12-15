def vigenere(text,key,option):
  alphabet="abcdefghijklmnopqrstuvwxyz " #Our alphabet, you can use this without space too
  len_alphabet=len(alphabet)
  
  text=text.lower()
  key=key.lower()
  
  len_text=len(text)
  len_key=len(key)

  result=""

  pos=0

  new_key=""

  if len_text>len_key:
    len_new_key=(len_text//len_key)+1
    new_key=len_new_key*key
  else:
    new_key=key

  for i in range (0,len_text):
    pos_text=alphabet.index(text[i])
    pos_key=alphabet.index(new_key[i])

    if option=="encrypt":
      pos=pos_text+pos_key
    else:
      pos=pos_text-pos_key
    if pos<len_alphabet:
      result+=alphabet[pos]
    else:
      result+=alphabet[pos%len_alphabet]

  print("Result text: ", result.lower())

  return


text=input("Enter text to encrypt: ")
key=input("Enter key: ")
vigenere(text,key,"encrypt")

print()
text=input("Enter text to decrypt: ")
key=input("Enter key: ")
vigenere(text,key,"decrypt")