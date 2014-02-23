# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(text):
    #In case we are not starting with a tag
    start = 0 if text[0] != '<' else text.find('>') + 1
    end = text.find('<', start) if text.find('<', start) != -1 else len(text)
    result = text[start : end].split()

    # This will work based on the assumption named in the question, in general not so sure
    while start < end:
        text = text[end:]
        start = text.find('>')
        end = text.find('<', start)
        if text.find('<', start) != -1:
            result.extend(text[start + 1: end].split())
        else:   # takes care of 1 of the cases,(see last added test)
            result.extend(text[start + 1 :].split())
    
    return result

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

print (remove_tags("This <i>line</i> has <em>lots</em> of <b>tags</b>."))
#>>> ['This', 'line', 'has', 'lots', 'of', 'tags', '.']
