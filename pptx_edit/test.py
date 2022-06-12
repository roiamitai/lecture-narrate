import os
import unittest
from .presentation import Presentation
#
BASIC_PRES_FILENAME = os.path.join(os.path.dirname(__file__),'test-resources','basic-pres.pptx')
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
#
class PptxOoxmlOpsTest (unittest.TestCase):
    #
    ...
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