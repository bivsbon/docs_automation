from PIL import Image
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import warnings
import cv2

warnings.filterwarnings("ignore")


class TextRecognizer:
    def __init__(self, weights_path):
        config = Cfg.load_config_from_name('vgg_transformer')
        config['weights'] = weights_path
        config['cnn']['pretrained'] = False
        config['device'] = 'cpu'
        config['predictor']['beamsearch'] = False

        self.detector = Predictor(config)

    def predict(self, img_cv):
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img_cv)
        s = self.detector.predict(img)
        return s
