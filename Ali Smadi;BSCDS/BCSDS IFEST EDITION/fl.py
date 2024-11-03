from ultralytics import YOLO    
from matplotlib import pyplot as plt
import numpy as np
m = YOLO('best.pt')
i = ''
r = m(np.array('tis.png'))
plt.imsave('f.png',r[0].plot())