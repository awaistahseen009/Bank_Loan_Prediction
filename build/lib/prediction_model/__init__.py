import os
from prediction_model.config import config
with open(os.path.join(config.PAKAGE_ROOT, 'VERSION')) as f :
    __version__ = f.read().strip()