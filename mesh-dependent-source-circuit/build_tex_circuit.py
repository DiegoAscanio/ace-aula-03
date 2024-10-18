from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import os
import sys

cwd = os.getcwd()

# Render the LaTeX to a PDF using pdflatex
import subprocess
subprocess.run(["pdflatex", "-output-directory=" + cwd + "/latex.out", "" + cwd + "/" + sys.argv[1]])

# Convert the generated PDF to PNG for display
subprocess.run(["convert", "-density", "300", "" + cwd + "/latex.out/" + sys.argv[1].replace('.tex', '.pdf'), "-quality", "90", "" + cwd + "/" + sys.argv[1].replace(".tex", ".png")])

# Load the image and display it
'''
img = mpimg.imread("" + cwd + "/circuit.png")
plt.figure(figsize=(6, 6))
plt.imshow(img)
plt.axis('off')
plt.show()
'''
