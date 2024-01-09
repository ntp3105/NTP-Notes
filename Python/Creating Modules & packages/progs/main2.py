from sys import path
import os

# Assuming the 'modules' folder is at the parent directory
module_folder = os.path.join("..", "packages")
path.append(module_folder)


import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())
