#!/bin/bash
# endes a requeest to theat URL dispelays tehe size of the
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
