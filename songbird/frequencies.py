#Functions to return 

freq = np.zeros(24, dtype=float)
A_calib = 440 #Hz
for i in range(0,24,1):
  freq[i] = A_calib*(2**((i-21)/12))

  def Major(tonic="C"):
  skips = [0,2,4,5,7,9,11,12]
  root_note_index = index_in_keyboard(tonic)
  scale = np.zeros(len(skips)+1, dtype=float)
  for i in range(len(skips)):
   scale[i] = freq[root_note_index+skips[i]]
  return scale

  def Minor(tonic="C"):
  skips = [0,2,3,5,7,8,10,12]
  root_note_index = index_in_keyboard(tonic)
  scale = np.zeros(len(skips)+1, dtype=float)
  for i in range(len(skips)):
   scale[i] = freq[root_note_index+skips[i]]
  return scale
  
  def MajorPenta(tonic="C"):
  skips = [0,2,4,7,9,12]
  root_note_index = index_in_keyboard(tonic)
  scale = np.zeros(len(skips)+1, dtype=float)
  for i in range(len(skips)):
   scale[i] = freq[root_note_index+skips[i]]
  return scale

  def MinorPenta(tonic="C"):
  skips = [0,3,5,7,10,12]
  root_note_index = index_in_keyboard(tonic)
  scale = np.zeros(len(skips)+1, dtype=float)
  for i in range(len(skips)):
   scale[i] = freq[root_note_index+skips[i]]
  return scale

  def Egyptian(tonic="C"):
  skips = [0,2,5,7,10,12]
  root_note_index = index_in_keyboard(tonic)
  scale = np.zeros(len(skips)+1, dtype=float)
  for i in range(len(skips)):
   scale[i] = freq[root_note_index+skips[i]]
  return scale

  def _index_in_keyboard(num):
  switch={
    "C":0,
    "C#":1,
    "D":2,
    "D#":3,
    "Eb":3,
    "E":4,
    "F":5,
    "F#":6,
    "Gb":6,
    "G":7,
    "G#":8,
    "Ab":8,
    "A":9,
    "A#":10,
    "Bb":10,
    "B":11,
    }
  return switch.get(num,"Invalid Input")