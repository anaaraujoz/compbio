# Computational Biology with Python
A centralized markdown for collecting notes as i follow Mike Saint-Antoine's youtube series, found at [https://www.youtube.com/playlist?list=PLWVKUEZ25V94kdT2Lh97KqB9MoLV9ZzmU].


## Lesson 1
### Central Dogma of Biology
- DNA has sections of instrutions for the building of messenger RNA (Transcription);
- Messenger RNA is used for making proteins (Translation);
- DNA -> transcription -> mRNA -> translation -> Protein
### Modelling the Central Dogma as Ordinary Differential Equations
- rate of transcription is:
  - dm/dt = production of mrna - rate of degradation * abundance of mrna
- rate of translation is:
  - dp/dt = (protein production * abundance of mrna) - (rate of degradation * protein abundance)

### In Python