def fileToStr(fileName):
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def main():
    title = 'Audio demo'
    player = 'Player goes here'
    contents = fileToStr('indexTemplate.html').format(**locals())   # NEW
    strToFile(contents, 'html/index.html')

main()