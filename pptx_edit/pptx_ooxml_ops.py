#
from lxml import etree
import os
#
# Paths into the standard PPTX OOXML extracted archive directory structure.
OOXML_APP_REL_FILENAME = os.path.join('docProps','app.xml')
OOXML_CONTENT_TYPE_REL_FILENAME = os.path.join('[Content_Types].xml')
OOXML_SLIDE_REL_REL_FILENAME = os.path.join('ppt','slides','_rels','slide1.xml.rels')
OOXML_SLIDE_REL_FILENAME = os.path.join('ppt','slides','slide1.xml')
#
# I use a manually edited and validated .pptx extracted file as a reference for XML
# snippets i need. It's easier that way, instead of storing them separately since
# the XML parsing is hierarchical and things like namespaces are lost when children
# are extracted from their parent's context.
REF_OOXML_DIRNAME = os.path.join(os.path.dirname(__file__),'ref-ooxml-extracted-pptx')
REF_OOXML_APP_FILENAME = os.path.join(REF_OOXML_DIRNAME,OOXML_APP_REL_FILENAME)
REF_OOXML_CONTENT_TYPE_FILENAME = os.path.join(REF_OOXML_DIRNAME,OOXML_CONTENT_TYPE_REL_FILENAME)
REF_OOXML_SLIDE_REL_FILENAME = os.path.join(REF_OOXML_DIRNAME,OOXML_SLIDE_REL_REL_FILENAME)
REF_OOXML_SLIDE_FILENAME = os.path.join(REF_OOXML_DIRNAME,OOXML_SLIDE_REL_FILENAME)
#
XPATH_CONTENT_TYPE_PARENT = '/Types'
XPATH_CONTENT_TYPE_MP3_DECL = '/Types.Default[@Extension=\'mp3\']'
XPATH_CONTENT_TYPE_PNG_DECL = '/Types.Default[@Extension=\'png\']'
#
try:
    root = etree.parse(REF_OOXML_CONTENT_TYPE_FILENAME)
    OOXML_MP3_CONTENT_TYPE_DECL_ELM = root.find(XPATH_CONTENT_TYPE_MP3_DECL)
    OOXML_PNG_CONTENT_TYPE_DECL_ELM = root.find(XPATH_CONTENT_TYPE_PNG_DECL)
finally:
    del root
# #
# XPATH_REL_AUDIO_DECL = ...
# #
# try:
#     et = etree.parse(REF_OOXML_SLIDE_REL_FILENAME).getroot()
#     root = et.getroot()
#     ...
# finally:
#     ...
#
def increment_presentation_media_counter (extract_root_dirname:str):
    et = etree.parse(os.path.join(extract_root_dirname,OOXML_APP_REL_FILENAME))
    root = et.getroot()
    count = int(root.findall('MMClips',root.nsmap)[0].text)
    root.findall('MMClips',root.nsmap)[0].text = str(count+1)
    et.write(os.path.join(extract_root_dirname,OOXML_APP_REL_FILENAME))
#
def update_presentation_audio_content_type_decl (extract_root_dirname:str):
    et = etree.parse(os.path.join(extract_root_dirname,OOXML_CONTENT_TYPE_REL_FILENAME))
    root = et.getroot()
    if not root.find(XPATH_CONTENT_TYPE_MP3_DECL,root.nsmap):
        root.find(XPATH_CONTENT_TYPE_PARENT).append(OOXML_MP3_CONTENT_TYPE_DECL_ELM)
    if not root.find(XPATH_CONTENT_TYPE_PNG_DECL,root.nsmap):
        root.find(XPATH_CONTENT_TYPE_PARENT).append(OOXML_PNG_CONTENT_TYPE_DECL_ELM)
#