(TeX-add-style-hook
 "index"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("hyperref" "hidelinks") ("geometry" "left=3cm" "right=3cm" "top=3cm" "bottom=3cm") ("adjustbox" "export")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "hyperref"
    "geometry"
    "titlesec"
    "indentfirst"
    "adjustbox"
    "float"
    "multicol"
    "tcolorbox"
    "framed"
    "xcolor"
    "xpatch"
    "fancyhdr"
    "etoolbox"
    "longtable"
    "array"
    "multirow"
    "gensymb"
    "amsmath"
    "graphicx"
    "tikz"
    "tikz-feynman")
   (TeX-add-symbols
    "columnseprulecolor")
   (LaTeX-add-labels
    "sec:orgb6a1330"
    "sec:org8816561"
    "sec:org4c95c8e"
    "sec:orgd3be5c8"
    "sec:org51331a9"
    "sec:orgb71f2c6"
    "sec:orge1f2446"
    "sec:org16e4083"
    "sec:org20c2c6e"
    "sec:org69bd142"
    "sec:org46aa63e"
    "sec:org38b9363"
    "sec:org41ad94b"
    "sec:org947eb40"
    "sec:orgf8d8e35"
    "sec:org78684dc"
    "sec:orgca617a4"
    "sec:org92fbf10"
    "sec:org32d0811"
    "sec:org787d4ac"
    "sec:org52e76ff"
    "sec:org181363a"
    "sec:org9461a07"
    "sec:org8bbc3ca"
    "sec:org1d908e7"
    "sec:org2953491"
    "sec:org6b93bf1"
    "sec:org8d9a627"
    "sec:org67a0f43"
    "sec:orgd8d9f07"
    "img:photoelectric_graph"
    "sec:org295e4f6"
    "sec:org3abcbdf"
    "sec:org0de0402"
    "img:energy_levels"
    "sec:org1d816f8"
    "img:electron_diffraction"
    "sec:org0f8e89b"
    "sec:orgcba1052"
    "sec:org2931dc0"
    "sec:org6885fe5"
    "sec:org0264ae8"
    "sec:org72eb266"
    "sec:org5de0691"
    "sec:org10fb387"
    "sec:org5e91145"
    "sec:org1995df2"
    "sec:org1de8540"
    "sec:orge83eb1e"
    "sec:org0f53197"
    "sec:orgdd9c304"
    "sec:orgc3edff3"
    "sec:org81396e7"
    "sec:org882cff6"
    "sec:org550409a"
    "sec:orgc580b2d"
    "sec:orge621d87"
    "sec:orgee5967a"
    "sec:orgb549453"
    "sec:orge746d37"
    "sec:org1965f3d"
    "sec:org5c53703"
    "sec:org90bad98"
    "sec:org7dc9453"
    "sec:orgeebad76"
    "sec:orgeccf0ce"
    "sec:org8b6254b"
    "sec:org37a98ba"
    "sec:org58edb7c"
    "sec:orgb25dbb6"))
 :latex)

