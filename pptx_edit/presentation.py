import tempfile
import zipfile
import typing
from .pptx_ooxml_ops import increment_presentation_media_counter
#
class Presentation:
    #
    def __init__(self,filename:str):
        self.extract_tempdir = tempfile.TemporaryDirectory()
        with zipfile.ZipFile((filename)) as zip:
            zip.extractall(self.extract_tempdir.name)
    #
    def slide_insert_audio (self,slide_idx:int,audio_fp:typing.BinaryIO):
        
        
        
        # FIXME When only updating, don't increment.
        increment_presentation_media_counter(self.extract_tempdir.name)
            
            
#