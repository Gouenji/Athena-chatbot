import os
with open('./aiml/train.aiml','r+') as training_file:
    training_file.seek(-10,2)
    training_file.write("<category>\n\
<pattern>*</pattern>\n\
<that>WHAT IS YOUR PASSWORD</that>\n\
<template>\n\
Thank you.\n\
</template>\n\
</category>\n")
    training_file.write("</aiml>")

