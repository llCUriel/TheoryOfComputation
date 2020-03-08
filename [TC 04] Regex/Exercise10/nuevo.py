import re 

def multiple_replace(dict, text):
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 



text = "_ _ _ _ _ _                    _"

dict = {
"_" : " ",
" " : "_",
}
print text +"\n"
print multiple_replace(dict, text)



