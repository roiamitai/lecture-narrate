#
from lxml import etree
import os
#
# TODO Move to defs.py file.
# TODO Prefix names with PPTX.
# Paths into the standard PPTX OOXML extracted archive directory structure.
OOXML_APP_REL_FILENAME = os.path.join('docProps','app.xml')
OOXML_CONTENT_TYPE_REL_FILENAME = os.path.join('[Content_Types].xml')
OOXML_SLIDE_REL_REL_FILENAME = os.path.join('ppt','slides','_rels','slide1.xml.rels')
OOXML_SLIDE_REL_FILENAME = os.path.join('ppt','slides','slide1.xml')
#
# TODO Prefix names with PPTX.
OOXML_AUDIO_CONTENT_TYPES = etree.parse(os.path.join(os.path.dirname(__file__),'xml-snippets','audio-content-types.xml'))
OOXML_SLIDE_AUDIO_RELS = etree.parse(os.path.join(os.path.dirname(__file__),'xml-snippets','slide-audio-rels.xml'))
OOXML_AUDIO_SHAPE = etree.parse(os.path.join(os.path.dirname(__file__),'xml-snippets','audio-shape.xml'))
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
    if not root.find('/Types/Default[@Extension=\'mp3\']',root.nsmap):
        root.find('/Types').append(OOXML_AUDIO_CONTENT_TYPES.find('/Types/Default[@Extension=\'mp3\']',OOXML_AUDIO_CONTENT_TYPES.nsmap))
    if not root.find('/Types/Default[@Extension=\'png\']',root.nsmap):
        root.find('/Types').append(OOXML_AUDIO_CONTENT_TYPES.find('/Types/Default[@Extension=\'png\']',OOXML_AUDIO_CONTENT_TYPES.nsmap))
#