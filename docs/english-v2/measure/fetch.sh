#!/bin/sh
# Fetch the four source texts the measurements in this directory run over.
# Nothing here is committed: data/ is in .gitignore terms "downloaded, untrusted".
set -e
cd "$(dirname "$0")" && mkdir -p data && cd data
curl -sL -o cmudict.dict https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict
curl -sL -o cmudict_LICENSE https://raw.githubusercontent.com/cmusphinx/cmudict/master/LICENSE
curl -sL -o pg1342.txt https://www.gutenberg.org/cache/epub/1342/pg1342.txt      # Pride and Prejudice
curl -sL -o pg844.txt  https://www.gutenberg.org/cache/epub/844/pg844.txt        # The Importance of Being Earnest
curl -sL -o mobypos.txt https://www.gutenberg.org/files/3203/files/mobypos.txt   # Moby Part-of-Speech, public domain
ls -la
