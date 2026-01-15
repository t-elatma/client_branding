


frappe.after_ajax(() => {
    frappe.call({
        method: "client_branding.api.get_branding",
        callback: (r) => {
            if (!r.message) return;

            const b = r.message;
            console.log(b);

            applyLogo(b.logo);
            applyColors(b.primary_color, b.secondary_color);
            applyFavicon(b.favicon);
            applyCustomCSS(b.custom_css);
        }
    });
});

/* -------------------------------
   Branding helpers
-------------------------------- */

function applyLogo(logo) {
    if (!logo) return;

    const logoImg = document.querySelector(".navbar-home img");
    if (logoImg) {
        logoImg.src = logo;
    }
}

function applyColors(primary, secondary) {
    if (primary) {
        document.documentElement.style.setProperty(
            "--brand-primary",
            primary
        );
    }

    if (secondary) {
        document.documentElement.style.setProperty(
            "--brand-secondary",
            secondary
        );
    }
}

function applyFavicon(favicon) {
    if (!favicon) return;

    // Remove all existing favicon links
    const links = document.querySelectorAll("link[rel~='icon']");
    links.forEach(link => link.remove());

    // Force cache busting
    const cacheBustedUrl = favicon + "?v=" + Date.now();

    // Add new favicon
    const newLink = document.createElement("link");
    newLink.rel = "icon";
    newLink.type = "image/png";
    newLink.href = cacheBustedUrl;

    document.head.appendChild(newLink);
}

function applyCustomCSS(css) {
    if (!css) return;

    const style = document.createElement("style");
    style.setAttribute("data-client-branding", "true");
    style.innerHTML = css;
    document.head.appendChild(style);
}
