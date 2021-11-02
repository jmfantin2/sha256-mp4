import os
from Crypto.Hash import SHA256

# input vars > you can alter these <
VIDEO = 'sha1.mp4'
CHUNK = 1024
# calculus vars 
FILE_SIZE = os.path.getsize(VIDEO)
LAST_CHUNK = FILE_SIZE % CHUNK

def run():
  
  print('\nvideo in:  ', VIDEO)
  print('file size: ', str(int(FILE_SIZE/1024))+'KB')
  print('chunk size:', str(CHUNK)+'B')
  print('last chunk:', str(LAST_CHUNK)+'B')
  
  print('\nloading...')

  hash_h0 = getHash()
  print('\nh0 hex: ' + hash_h0.hex())
    
# build and update h0 until reaching BOF
def getHash():
  
  h0 = ''
  
  with open(VIDEO,'rb') as file:

    # verifies if last chunk is shorter than chunk size
    shorter_last = False
    if LAST_CHUNK > 0:
      shorter_last = True
     
    last_position = FILE_SIZE
    # iterates from size to zero
    while last_position > 0:

      size = CHUNK  

      if shorter_last:
      # update size so last_position doesn't mismatch
        size = LAST_CHUNK
        shorter_last = False # turn off the flag :) 
      
      #this should be the start of the current chunk
      last_position -= size  
      # use seek pointer for file position tracking
      file.seek(last_position)
      chunk_data = file.read(CHUNK) # read that chunk
      
      # SHA-256: updates until reaching h0 for integrity
      # https://pycryptodome.readthedocs.io/en/latest/src/hash/sha256.html
      sha256 = SHA256.new()
      sha256.update(chunk_data)
      if h0 != '': sha256.update(h0)
      h0 = sha256.digest()
        
  return h0

if __name__ == "__main__":
  run()