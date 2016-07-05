from tightocr.adapters.api_adapter import TessApi
from tightocr.adapters.lept_adapter import pix_read
from tightocr.constants import RIL_PARA
 
t = TessApi(None, 'dan');
p = pix_read('test.png')
t.set_image_pix(p)
t.recognize()
 
#if t.mean_text_confidence() < 85:
#    raise Exception("Too much error.")
 
for block in t.iterate(RIL_PARA):
    print(block)