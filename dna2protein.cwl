class: Workflow
cwlVersion: v1.0
id: dna2protein_cwl
label: dna2protein.cwl.yaml
inputs:
  - id: dna
    type: File
    fileTypes: []
    'sbg:x': -683.9168701171875
    'sbg:y': -74.864013671875
outputs:
  - id: rna
    outputSource:
      - transcribe/rna
    type: File
    fileTypes: []
    'sbg:x': -116.9168701171875
    'sbg:y': -206.864013671875
  - id: protein
    outputSource:
      - translate/protein
    type: File
    fileTypes: []
    'sbg:x': 170.0831298828125
    'sbg:y': -76.864013671875
steps:
  - id: transcribe
    in:
      - id: dna
        source:
          - dna
      - id: verbose_transcribe
        default: true
    out:
      - id: rna
    run:
      class: CommandLineTool
      cwlVersion: v1.0
      baseCommand:
        - transcribe.py
      inputs:
        - type: File
          id: dna
          inputBinding:
            position: 1
          doc: DNA input file to transcribe
          secondaryFiles: []
        - default: false
          type: boolean?
          id: verbose_transcribe
          inputBinding:
            prefix: '--verbose'
            separate: true
          secondaryFiles: []
      outputs:
        - id: rna
          type: File
          outputBinding:
            glob: rna.txt
      id: transcribe
      requirements:
        - class: DockerRequirement
          dockerPull: 'sevenbridges/dna2protein:0.5.5'
        - class: InitialWorkDirRequirement
          listing: []
      stdout: transcribe.log
      'sbg:job':
        inputs:
          dna:
            class: File
            path: /path/to/dna.ext
            secondaryFiles: []
            size: 0
          verbose: true
      'sbg:modified': true
    'sbg:x': -402.9168701171875
    'sbg:y': -74.864013671875
  - id: translate
    in:
      - id: mRNA
        source:
          - transcribe/rna
      - id: verbose_translate
        default: true
    out:
      - id: protein
    run:
      class: CommandLineTool
      cwlVersion: v1.0
      baseCommand:
        - translate.py
      inputs:
        - type: File
          id: mRNA
          inputBinding:
            position: 1
          doc: mRNA to transcribe
          secondaryFiles: []
        - default: false
          type: boolean?
          id: verbose_translate
          inputBinding:
            prefix: '-v'
            separate: true
          doc: Run in verbose mode
          secondaryFiles: []
      outputs:
        - id: protein
          type: File
          outputBinding:
            glob: protein.txt
      id: translate
      requirements:
        - class: InitialWorkDirRequirement
          listing: []
      stdout: translate.log
      'sbg:job':
        inputs: {}
        runtime: {}
      'sbg:modified': true
    'sbg:x': -128.9168701171875
    'sbg:y': -83.864013671875
description: ''
'sbg:modified': true
