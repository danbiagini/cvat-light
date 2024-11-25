# Overlaying production
from cvat.settings.production import *

# Add the $CVAT_HOST to the CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [f"https://{os.getenv('CVAT_HOST')}"]
