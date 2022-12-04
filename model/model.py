from PIL import Image
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import warnings

warnings.filterwarnings("ignore")


def predict(img):
    im = Image.open(img)
    config = Cfg.load_config_from_name('vgg_transformer')
    config['weights'] = './weights.pth'
    config['cnn']['pretrained'] = False
    config['device'] = 'cpu'
    config['predictor']['beamsearch'] = False

    detector = Predictor(config)
    s = detector.predict(im)
    print(s)
    return s


predict('1.jpg')

