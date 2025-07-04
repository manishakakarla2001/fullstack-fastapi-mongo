#!/bin/sh

echo "🚀 Replacing env variables in env.js..."

# Replace ${API_URL} with actual value and output to env.js
envsubst '${API_URL}' < /usr/share/nginx/html/env.template.js > /usr/share/nginx/html/env.js

# Start nginx in foreground
exec nginx -g 'daemon off;'
