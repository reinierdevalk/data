- each project folder contains the following four folders
  - score/
    - contains, when using using own-made data (adriaenssen, byrd)
      - (.pdf files of vocal model, from which are created)
        - full .sib scores (CMN + tab) of vocal model, from which are created
          - (no_tab .sib scores: CMN only, for .mid files export)
          - (tab_only .sib scores: tab only, for .tab files export)
    - contains, when using existing data (josquin)
      - .pdf files of vocal model
  - in/
    - contains
      - MIDI/
        - contains .mid files, either self-exported or existing
        - same piece names/naming convention as in tab/ (if self-exported)
      - tab/
        - contains
          - .tc files (existing) or .tab files (self-exported), from which are created
          - .tbp files
        - same piece names/naming convention as in in/MIDI/ (if self-exported)
  - out/

- to run voice separation experiment on TabMapper-created data
  - move files to data/annotated/voice_separation/
    .tbp file in data/annotated/tabmapper/<dataset>/tab/ to
                 data/annotated/voice_separation/encodings/<dataset>
    .mid file in data/annotated/tabmapper/<dataset>/mapped/ goes to
                 data/annotated/voice_separation/MIDI/<dataset>
  - run experiment
  - move files back to data/annotated/tabmapper/