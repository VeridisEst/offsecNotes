#! /bin/bash

find ./ -iname "*.md" -type f -exec sh -c 'pandoc "${0}" -o "../PDFs/$(basename ${0%.md}.pdf)"' {} \;

#find ./ -iname "*.md" -type f -exec sh -c 'pandoc "${0}" -o "${0%.md}.pdf"' {} \;
