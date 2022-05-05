import os
import constants

# Erschaffe notwendiges Dateisystem
os.mkdir(os.path.join(os.getcwd(), constants.SIGNALS))
os.mkdir(os.path.join(os.getcwd(), constants.LOGS))
