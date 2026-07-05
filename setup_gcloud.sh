#!/usr/bin/env bash
# One-time Google Cloud setup for CivicPulse AI using the gcloud CLI.
# Usage:  ./setup_gcloud.sh YOUR_PROJECT_ID [REGION]
set -euo pipefail

PROJECT_ID="${1:-}"
REGION="${2:-us-central1}"

if [[ -z "${PROJECT_ID}" ]]; then
  echo "Usage: ./setup_gcloud.sh YOUR_PROJECT_ID [REGION]"
  exit 1
fi

echo "==> Authenticating (opens a browser)..."
gcloud auth login

echo "==> Setting active project to ${PROJECT_ID}..."
gcloud config set project "${PROJECT_ID}"
gcloud config set run/region "${REGION}"

echo "==> Enabling required APIs (Cloud Run, Vertex AI, Cloud Build, Artifact Registry)..."
gcloud services enable \
  run.googleapis.com \
  aiplatform.googleapis.com \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com

echo "==> (Optional) Application Default Credentials for local Vertex AI testing..."
echo "    Run this if you plan to use Vertex AI locally:"
echo "    gcloud auth application-default login"

echo "==> Done. Project '${PROJECT_ID}' is ready in region '${REGION}'."
echo "    Next: ./deploy.sh ${PROJECT_ID} ${REGION}"
