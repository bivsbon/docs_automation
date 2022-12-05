from PIL import Image
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import warnings
import cv2

warnings.filterwarnings("ignore")


def predict(img_cv):
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img_cv)
    config = Cfg.load_config_from_name('vgg_transformer')
    config['weights'] = './weights.pth'
    config['cnn']['pretrained'] = False
    config['device'] = 'cpu'
    config['predictor']['beamsearch'] = False

    detector = Predictor(config)
    s = detector.predict(img)
    return s
