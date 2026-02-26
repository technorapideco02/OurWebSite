// Inlined configuration for Service Worker
const SITE_CONFIG = {
    acl: {
        allowed: [
            "/",
            "/index.html",
            "/web-development",
            "/android-application",
            "/ios-app-development",
            "/cloud-solution",
            "/n8n-automation",
            "/portfolio",
            "/our-designs",
            "/about",
            "/insights",
            "/blog-details",
            "/casestudy",
            "/home",
            "/public",
            "/config.js",
            "/sw.js",
            "/sitemap.xml",
            "/robots.txt",
            "/style.css",
            "/script.js",
            "/favicon_io",
            "/favicon.ico"
        ],
        denied: [
            "/.vscode",
            "/.git",
            "/.gemini"
        ]
    }
};

self.addEventListener("install", e => {
    self.skipWaiting();
});

self.addEventListener("activate", e => {
    e.waitUntil(self.clients.claim());
});

self.addEventListener("fetch", e => {
    const url = new URL(e.request.url);
    const path = url.pathname;

    // Check denied paths
    if (SITE_CONFIG.acl.denied.some(deniedPath => path.endsWith(deniedPath))) {
        return e.respondWith(
            new Response(`<h1>403 Forbidden</h1><p>Access to ${path} is restricted by site policy.</p>`, {
                status: 403,
                statusText: "Forbidden",
                headers: { "Content-Type": "text/html" }
            })
        );
    }

    // Check allowed paths for navigation requests
    if (e.request.mode === "navigate") {
        const scopePath = new URL(self.registration.scope).pathname;
        const relativePath = path.startsWith(scopePath) ? path.substring(scopePath.length - 1) : path;

        const isAllowed = SITE_CONFIG.acl.allowed.some(allowedPath => {
            if (allowedPath === "/") {
                return relativePath === "/" || relativePath === "/index.html";
            }
            return relativePath.startsWith(allowedPath);
        });

        if (!isAllowed) {
            return e.respondWith(
                new Response(`<h1>404 Not Found</h1><p>The requested path is not available.</p><a href="/">Go Home</a>`, {
                    status: 404,
                    statusText: "Not Found",
                    headers: { "Content-Type": "text/html" }
                })
            );
        }
    }

    e.respondWith(fetch(e.request));
});
