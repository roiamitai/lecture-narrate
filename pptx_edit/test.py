import os
import unittest
import tempfile
import shutil
from lxml import etree
from .ops import increment_presentation_media_counter
from .ops import OOXML_APP_REL_FILENAME
from .ops import OOXML_CONTENT_TYPE_REL_FILENAME
from .ops import OOXML_SLIDE_REL_REL_FILENAME
from .ops import OOXML_SLIDE_REL_FILENAME
from .presentation import Presentation
#
BASIC_PRES_FILENAME = os.path.join(os.path.dirname(__file__),'test-resources','basic-pres.pptx')
ORIGINAL_UNZIP_PRES_DIRNAME = os.path(os.path.dirname(__file__),'test-resources','no-audio-pres-unzipped')
EXPECTED_UNZIP_PRES_DIRNAME = os.path(os.path.dirname(__file__),'test-resources','with-audio-pres-unzipped')
#
class PptxOoxmlOpsTest (unittest.TestCase):
    #
    def setUp(self) -> None:
        self.original_mutable_copy = tempfile.TemporaryDirectory()
        self.doCleanups(self.original_mutable_copy.cleanup)
        shutil.copytree(ORIGINAL_UNZIP_PRES_DIRNAME,self.original_mutable_copy.name)
        self.original_pres_unzip_dirname = self.original_mutable_copy.name
    #
    def test_increment_presentation_media_counter (self):
        increment_presentation_media_counter (self.original_pres_unzip_dirname)
        
        
#
class ZipFileHandlingTest (unittest.TestCase):
    #
    def test_zipfile_load (self):
        Presentation(BASIC_PRES_FILENAME)
    #
    def test_original_zipfile_unchanged (self):
        with open(BASIC_PRES_FILENAME,'rb') as fp:
            original_content = fp.read()
        pres = Presentation(BASIC_PRES_FILENAME)
        pres.slide_insert_audio(None,None)# FIXME Arguments incorrect.
        with open(BASIC_PRES_FILENAME,'rb') as fp:
            subsequent_content = fp.read()
        self.assertEqual(original_content,subsequent_content)
#
class SlideAudioInsertionTest (unittest.TestCase):
    #
    def test_single_slide_pres_insertion (self):
        
        raise NotImplemented()
        
        pres = Presentation(BASIC_PRES_FILENAME)
        ...
        ...
        pres.slide_insert_audio(None,None)
        
        # TODO Compare extracted folder aginst manually edited and validated, reference version. Maybe compare zipped?
    #
    def test_multi_slide_pres_insertion (self): raise NotImplemented()
    #
    def test_slide_subset_insertion (self): raise NotImplemented()
    #
    def test_replacement (self): raise NotImplemented()
#