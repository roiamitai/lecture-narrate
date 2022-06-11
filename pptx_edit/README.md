# Easily diff the effects of a certain edit on a PPTX file
Unzip the *.pptx file.  
Use the following Python snippet from root directory:

    import os
    import lxml.etree as etree
    for file in [os.path.abspath(os.path.join(root,file)) for root,dirs,files in os.walk('.') for file in files if '.xml' in file]:
        etree.parse(file).write(file,pretty_print=True)