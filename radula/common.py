import os

version = 0.1
confdir = os.path.expanduser('~/.radula')

def create_dir():
  try:
    os.makedirs(confdir)
  except OSError:
    if (os.path.isdir(confdir)):
      pass
    else:
      raise


