#!/bin/bash

if [ -z "$1" ]; then
  echo "Use: $0 <version> (ex: 10_10 or 10_11)"
  exit 1
fi

VERSION="$1"

openapi-generator-cli generate -g python \
  -t ./templates/python \
  -i ./specs/openapi_${VERSION}.json \
  -p packageName=jellyfin.generated.api_${VERSION},packageVersion=${VERSION/_/.} \
  -o ./src/