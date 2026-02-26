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

if (typeof self !== "undefined") {
    self.SITE_CONFIG = SITE_CONFIG;
}
if (typeof window !== "undefined") {
    window.SITE_CONFIG = SITE_CONFIG;
}
