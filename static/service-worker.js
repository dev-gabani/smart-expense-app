const CACHE_NAME = 'smart-expense-v2';
const ASSETS_TO_CACHE = [
  '/static/css/style.css',
  '/static/icon.png',
  '/static/manifest.json',
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css',
  'https://cdn.jsdelivr.net/npm/chart.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            return caches.delete(cache);
          }
        })
      );
    })
  );
});

self.addEventListener('fetch', event => {
  // For static assets, try cache first, then network
  if (event.request.url.includes('/static/') || event.request.url.includes('cdnjs') || event.request.url.includes('cdn.jsdelivr')) {
    event.respondWith(
      caches.match(event.request).then(response => {
        return response || fetch(event.request);
      })
    );
  } else {
    // For all other requests (HTML, API), go to network first
    event.respondWith(
      fetch(event.request).catch(() => caches.match('/'))
    );
  }
});
