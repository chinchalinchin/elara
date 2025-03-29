#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

S3_BUCKET=$ELARA_BUCKET
DISTRIBUTION_ID=$ELARA_DIST
DIRECTORY="docs/build/html"
BUILD=false
INVALIDATE=false

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --bucket)
      S3_BUCKET="$2"
      shift 2
      ;;
    --src)
      DIRECTORY="$2"
      shift 2
      ;;
    --dist)
      DISTRIBUTION_ID="$2"
      shift 2
      ;;
    --build)
      BUILD=true
      shift
      ;;
    --invalidate)
      INVALIDATE=true
      shift
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

# Check if all required arguments are provided
if [ -z "$S3_BUCKET" ] || [ -z "$DIRECTORY" ] || [ -z "$DISTRIBUTION_ID" ]; then
  echo "Usage: $0 --bucket <s3_bucket_name> --src <directory> --dist <cloudfront_distribution_id> [--build]"
  exit 1
fi

# Perform the build if the --build flag is set
if $BUILD; then
  cd "$SCRIPT_DIR/docs"  # Change to the src directory
  if make clean && make html | grep -iE "ERROR|FAILED"; then
    echo "Build failed. Aborting deployment."
    exit 1
  fi
  cd "$SCRIPT_DIR"  # Change back to the original directory
fi

# Construct the full path to the directory
BUILD_DIR="$SCRIPT_DIR/$DIRECTORY"

aws s3 sync "$BUILD_DIR" "s3://$S3_BUCKET/" \
  --delete \
  --acl public-read

echo "Successfully copied contents of $TARGET_DIR to s3://$S3_BUCKET/"

# Invalidate the CloudFront cache.
if [ -n "DISTRIBUTION_ID" ] && $INVALIDATE; then 
    aws cloudfront create-invalidation \
        --distribution-id "$DISTRIBUTION_ID" \
        --paths "/*"
else
    echo "Skipping CloudFront invalidation."
fi

exit 0